"""
This module is the computational part of the geometrical module of ToFu
"""

# General common libraries
import numpy as np
import scipy.interpolate as scpinterp


# Less common libraries
import Polygon as plg

# ToFu-specific
try:
    import tofu.geom._def as _def
    import tofu.geom._GG as _GG
except Exception:
    from . import _def as _def
    from . import _GG as _GG



"""
###############################################################################
###############################################################################
                        Ves functions
###############################################################################
"""


############################################
#####       Ves sub-functions
############################################



def _Ves_set_Poly(Poly, arrayorder='C', Type='Tor', Lim=None, Clock=False):
    """ Prepare, format and compute all key geometrical attributes of a Ves object based on its Poly  """
    # Make Poly closed, counter-clockwise, with '(cc,N)' layout and good arrayorder
    Poly = _GG.Poly_Order(Poly, order='C', Clock=False, close=True, layout='(cc,N)', Test=True)
    assert Poly.shape[0]==2, "Arg Poly must be a 2D polygon !"
    NP = Poly.shape[1]
    P1Max = Poly[:,np.argmax(Poly[0,:])]
    P1Min = Poly[:,np.argmin(Poly[0,:])]
    P2Max = Poly[:,np.argmax(Poly[1,:])]
    P2Min = Poly[:,np.argmin(Poly[1,:])]
    BaryP = np.sum(Poly[:,:-1],axis=1,keepdims=False)/(Poly.shape[1]-1)
    BaryL = np.array([(P1Max[0]+P1Min[0])/2., (P2Max[1]+P2Min[1])/2.])
    TorP = plg.Polygon(Poly.T)
    Surf = TorP.area()
    BaryS = np.array(TorP.center()).flatten()
    if Type.lower()=='lin':
        assert hasattr(Lim,'__iter__') and len(Lim)==2 and Lim[1]>Lim[0], "Arg Lim must be a iterable of len()==2 sorted in increasing order !"
        Lim = np.asarray(Lim)
        Vol, BaryV = None, None
    else:
        Lim = None if Lim is None else np.asarray(Lim)
        Vol, BaryV = _GG.Poly_VolAngTor(Poly)
        assert Vol > 0., "Pb. with volume computation for Ves object of type 'Tor' !"
    # Compute the non-normalized vector of each side of the Poly
    Vect = np.diff(Poly,n=1,axis=1)
    Vect = np.ascontiguousarray(Vect) if arrayorder=='C' else np.asfortranarray(Vect)
    # Compute the normalised vectors directed inwards
    Vin = np.array([Vect[1,:],-Vect[0,:]]) if _GG.Poly_isClockwise(Poly) else np.array([-Vect[1,:],Vect[0,:]])
    Vin = Vin/np.tile(np.hypot(Vin[0,:],Vin[1,:]),(2,1))
    Vin = np.ascontiguousarray(Vin) if arrayorder=='C' else np.asfortranarray(Vin)
    poly = _GG.Poly_Order(Poly, order=arrayorder, Clock=Clock, close=True, layout='(cc,N)', Test=True)
    return poly, NP, P1Max, P1Min, P2Max, P2Min, BaryP, BaryL, Surf, BaryS, Lim, Vol, BaryV, Vect, Vin


def _Ves_get_InsideConvexPoly(Poly, P2Min, P2Max, BaryS, RelOff=_def.TorRelOff, ZLim='Def', Spline=True, Splprms=_def.TorSplprms, NP=_def.TorInsideNP, Plot=False, Test=True):
    if Test:
        assert type(RelOff) is float, "Arg RelOff must be a float"
        assert ZLim is None or ZLim=='Def' or type(ZLim) in [tuple,list], "Arg ZLim must be a tuple (ZlimMin, ZLimMax)"
        assert type(Spline) is bool, "Arg Spline must be a bool !"
    if not ZLim is None:
        if ZLim=='Def':
            ZLim = (P2Min[1]+0.1*(P2Max[1]-P2Min[1]), P2Max[1]-0.05*(P2Max[1]-P2Min[1]))
        indZLim = (Poly[1,:]<ZLim[0]) | (Poly[1,:]>ZLim[1])
        Poly = np.delete(Poly, indZLim.nonzero()[0], axis=1)
    if np.all(Poly[:,0]==Poly[:,-1]):
        Poly = Poly[:,:-1]
    Np = Poly.shape[1]
    if Spline:
        BarySbis = np.tile(BaryS,(Np,1)).T
        Ptemp = (1.-RelOff)*(Poly-BarySbis)
        #Poly = BarySbis + Ptemp
        Ang = np.arctan2(Ptemp[1,:],Ptemp[0,:])
        Ang, ind = np.unique(Ang, return_index=True)
        Ptemp = Ptemp[:,ind]
        # spline parameters
        ww = Splprms[0]*np.ones((Np+1,))
        ss = Splprms[1]*(Np+1) # smoothness parameter
        kk = Splprms[2] # spline order
        nest = int((Np+1)/2.) # estimate of number of knots needed (-1 = maximal)
        # Find the knot points

        #tckp,uu = scpinterp.splprep([np.append(Ptemp[0,:],Ptemp[0,0]),np.append(Ptemp[1,:],Ptemp[1,0]),np.append(Ang,Ang[0]+2.*np.pi)], w=ww, s=ss, k=kk, nest=nest)
        tckp,uu = scpinterp.splprep([np.append(Ptemp[0,:],Ptemp[0,0]),np.append(Ptemp[1,:],Ptemp[1,0])], u=np.append(Ang,Ang[0]+2.*np.pi), w=ww, s=ss, k=kk, nest=nest, full_output=0)
        xnew,ynew = scpinterp.splev(np.linspace(-np.pi,np.pi,NP),tckp)
        Poly = np.array([xnew+BaryS[0],ynew+BaryS[1]])
        Poly = np.concatenate((Poly,Poly[:,0:1]),axis=1)
    if Plot:
        f = plt.figure(facecolor='w',figsize=(8,10))
        ax = f.add_axes([0.1,0.1,0.8,0.8])
        ax.plot(Poly[0,:], Poly[1,:],'-k', Poly[0,:],Poly[1,:],'-r')
        ax.set_aspect(aspect="equal",adjustable='datalim'), ax.set_xlabel(r"R (m)"), ax.set_ylabel(r"Z (m)")
        f.canvas.draw()
    return Poly



def _Ves_get_meshEdge(VPoly, dL, DS=None, dLMode='abs', DIn=0., VIn=None, margin=1.e-9):
    types =[int,float,np.int32,np.int64,np.float32,np.float64]
    assert type(dL) in types and type(DIn) in types
    assert DS is None or (hasattr(DS,'__iter__') and len(DS)==2)
    if DS is None:
        DS = [None,None]
    else:
        assert all([ds is None or (hasattr(ds,'__iter__') and len(ds)==2 and all([ss is None or type(ss) in types for ss in ds])) for ds in DS])
    assert type(dLMode) is str and dLMode.lower() in ['abs','rel'], "Arg dLMode must be in ['abs','rel'] !" 
    #assert ind is None or (type(ind) is np.ndarray and ind.ndim==1 and ind.dtype in ['int32','int64'] and np.all(ind>=0)), "Arg ind must be None or 1D np.ndarray of positive int !"
    Pts, dLr, ind, N, Rref, VPolybis = _GG._Ves_Smesh_Cross(VPoly, float(dL), dLMode=dLMode.lower(), D1=DS[0], D2=DS[1], margin=margin, DIn=float(DIn), VIn=VIn)
    return Pts, dLr, ind



def _Ves_get_meshCross(VPoly, Min1, Max1, Min2, Max2, dS, DS=None, dSMode='abs', ind=None, margin=1.e-9):
    types =[int,float,np.int32,np.int64,np.float32,np.float64]
    assert type(dS) in types or (hasattr(dS,'__iter__') and len(dS)==2 and all([type(ds) in types for ds in dS])), "Arg dS must be a float or a list 2 floats !"
    dS = [float(dS),float(dS)] if type(dS) in types else [float(dS[0]),float(dS[1])]
    assert DS is None or (hasattr(DS,'__iter__') and len(DS)==2)
    if DS is None:
        DS = [None,None]
    else:
        assert all([ds is None or (hasattr(ds,'__iter__') and len(ds)==2 and all([ss is None or type(ss) in types for ss in ds])) for ds in DS])
    assert type(dSMode) is str and dSMode.lower() in ['abs','rel'], "Arg dSMode must be in ['abs','rel'] !"
    assert ind is None or (type(ind) is np.ndarray and ind.ndim==1 and ind.dtype in ['int32','int64'] and np.all(ind>=0)), "Arg ind must be None or 1D np.ndarray of positive int !"
    
    MinMax1 = np.array([Min1,Max1])
    MinMax2 = np.array([Min2,Max2])
    if ind is None:
        Pts, dS, ind, d1r, d2r = _GG._Ves_meshCross_FromD(MinMax1, MinMax2, dS[0], dS[1], D1=DS[0], D2=DS[1], dSMode=dSMode, VPoly=VPoly, margin=margin)
    else:
        assert type(ind) is np.ndarray and ind.ndim==1 and ind.dtype in ['int32','int64'] and np.all(ind>=0), "Arg ind must be a np.ndarray of int !"
        Pts, dS, d1r, d2r = _GG._Ves_meshCross_FromInd(MinMax1, MinMax2, dS[0], dS[1], ind, dSMode=dSMode, margin=margin)
    return Pts, dS, ind, (d1r,d2r)


def _Ves_get_meshV(VPoly, Min1, Max1, Min2, Max2, dV, DV=None, dVMode='abs', ind=None, VType='Tor', VLim=None, Out='(X,Y,Z)', margin=1.e-9):
    types =[int,float,np.int32,np.int64,np.float32,np.float64]
    assert type(dV) in types or (hasattr(dV,'__iter__') and len(dV)==3 and all([type(ds) in types for ds in dV])), "Arg dV must be a float or a list 3 floats !"
    dV = [float(dV),float(dV),float(dV)] if type(dV) in types else [float(dV[0]),float(dV[1]),float(dV[2])]
    assert DV is None or (hasattr(DV,'__iter__') and len(DV)==3)
    if DV is None:
        DV = [None,None,None]
    else:
        assert all([ds is None or (hasattr(ds,'__iter__') and len(ds)==2 and all([ss is None or type(ss) in types for ss in ds])) for ds in DV]), "Arg DV must be a list of 3 lists of 2 floats !"
    assert type(dVMode) is str and dVMode.lower() in ['abs','rel'], "Arg dVMode must be in ['abs','rel'] !"
    assert ind is None or (type(ind) is np.ndarray and ind.ndim==1 and ind.dtype in ['int32','int64'] and np.all(ind>=0)), "Arg ind must be None or 1D np.ndarray of positive int !"

    MinMax1 = np.array([Min1,Max1])
    MinMax2 = np.array([Min2,Max2])
    VLim = None if VType.lower()=='tor' else np.array(VLim)
    dVr = [None,None,None]
    if ind is None:
        if VType.lower()=='tor':
            Pts, dV, ind, dVr[0], dVr[1], dVr[2] = _GG._Ves_Vmesh_Tor_SubFromD_cython(dV[0], dV[1], dV[2], MinMax1, MinMax2, DR=DV[0], DZ=DV[1], DPhi=DV[2], VPoly=VPoly, Out=Out, margin=margin)
        else:
            Pts, dV, ind, dVr[0], dVr[1], dVr[2] = _GG._Ves_Vmesh_Lin_SubFromD_cython(dV[0], dV[1], dV[2], VLim, MinMax1, MinMax2, DX=DV[0], DY=DV[1], DZ=DV[2], VPoly=VPoly, margin=margin)
    else:
        if VType.lower()=='tor':
            Pts, dV, dVr[0], dVr[1], dVr[2] = _GG._Ves_Vmesh_Tor_SubFromInd_cython(dV[0], dV[1], dV[2], MinMax1, MinMax2, ind, Out=Out, margin=margin)
        else:
            Pts, dV, dVr[0], dVr[1], dVr[2] = _GG._Ves_Vmesh_Lin_SubFromInd_cython(dV[0], dV[1], dV[2], VLim, MinMax1, MinMax2, ind, margin=margin)
    return Pts, dV, ind, dVr


def _Ves_get_meshS(VPoly, Min1, Max1, Min2, Max2, dS, DS=None, dSMode='abs', ind=None, DIn=0., VIn=None, VType='Tor', VLim=None, Out='(X,Y,Z)', margin=1.e-9):
    types =[int,float,np.int32,np.int64,np.float32,np.float64]
    assert type(dS) in types or (hasattr(dS,'__iter__') and len(dS)==2 and all([type(ds) in types for ds in dS])), "Arg dS must be a float or a list 3 floats !"
    dS = [float(dS),float(dS),float(dS)] if type(dS) in types else [float(dS[0]),float(dS[1]),float(dS[2])]
    assert DS is None or (hasattr(DS,'__iter__') and len(DS)==3)
    if DS is None:
        DS = [None,None,None]
    else:
        assert all([ds is None or (hasattr(ds,'__iter__') and len(ds)==2 and all([ss is None or type(ss) in types for ss in ds])) for ds in DS]), "Arg DS must be a list of 3 lists of 2 floats !"
    assert type(dSMode) is str and dSMode.lower() in ['abs','rel'], "Arg dSMode must be in ['abs','rel'] !"
    assert ind is None or (type(ind) is np.ndarray and ind.ndim==1 and ind.dtype in ['int32','int64'] and np.all(ind>=0)), "Arg ind must be None or 1D np.ndarray of positive int !"

    MinMax1 = np.array([Min1,Max1])
    MinMax2 = np.array([Min2,Max2])
    VLim = np.array(VLim) if VLim is not None else VLim
    #VLim = None if VType.lower()=='tor' else np.array(VLim)    # Probably mistake
    dSr = [None,None]
    if ind is None:
        if VType.lower()=='tor':
            if VLim is None:
                Pts, dS, ind, NL, dSr[0], Rref, dSr[1], nRPhi0, VPbis = _GG._Ves_Smesh_Tor_SubFromD_cython(dS[0], dS[1], VPoly, DR=DS[0], DZ=DS[1], DPhi=DS[2], DIn=DIn, VIn=VIn, PhiMinMax=None, Out=Out, margin=margin)
            else:
                Pts, dS, ind, NL, dSr[0], Rref, dR0r, dZ0r, dSr[1], VPbis = _GG._Ves_Smesh_TorStruct_SubFromD_cython(VLim, dS[0], dS[1], VPoly, DR=DS[0], DZ=DS[1], DPhi=DS[2], DIn=DIn, VIn=VIn, Out=Out, margin=margin)
                dSr += [dR0r, dZ0r]
        else:
            Pts, dS, ind, NL, dSr[0], Rref, dSr[1], dY0r, dZ0r, VPbis = _GG._Ves_Smesh_Lin_SubFromD_cython(VLim, dS[0], dS[1], VPoly, DX=DS[0], DY=DS[1], DZ=DS[2], DIn=DIn, VIn=VIn, margin=margin)
            dSr += [dY0r, dZ0r]
    else:
        if VType.lower()=='tor':
            if VLim is None:
                Pts, dS, NL, dSr[0], Rref, dSr[1], nRPhi0, VPbis = _GG._Ves_Smesh_Tor_SubFromInd_cython(dS[0], dS[1], VPoly, ind, DIn=DIn, VIn=VIn, PhiMinMax=None, Out=Out, margin=margin)
            else:
                Pts, dS, NL, dSr[0], Rref, dR0r, dZ0r, dSr[1], VPbis = _GG._Ves_Smesh_TorStruct_SubFromInd_cython(VLim, dS[0], dS[1], VPoly, ind, DIn=DIn, VIn=VIn, Out=Out, margin=margin)
                dSr += [dR0r, dZ0r]
        else:
            Pts, dS, NL, dSr[0], Rref, dSr[1], dY0r, dZ0r, VPbis = _GG._Ves_Smesh_Lin_SubFromInd_cython(VLim, dS[0], dS[1], VPoly, ind, DIn=DIn, VIn=VIn, margin=margin)
            dSr += [dY0r, dZ0r]
    return Pts, dS, ind, dSr




"""
###############################################################################
###############################################################################
                        LOS functions
###############################################################################
"""

def LOS_calc_InOutPolProj(VType, VPoly, Vin, VLim, D, uu, Name, LSPoly=None, LSLim=None, LSVin=None):
    C1 = all([pp is None for pp in [LSPoly,LSLim,LSVin]])
    C2 = all([type(pp) is list and len(pp)==len(LSPoly)])
    assert C1 or C2, "Args LSPoly, LSLim and LSVin must be all None or list of the same len() of respectively Poly, Lim and VIn (i.e.: np.array, None or list, and np.ndarray) !"

    if VType.lower()=='tor':
        PIn, POut, VOut, IOut = GG.Calc_InOut_LOS_PIO_new(D.reshape((3,1)), uu.reshape((3,1)), np.ascontiguousarray(VPoly), np.ascontiguousarray(Vin))
        #kPIn =
        #kPOut =
        if not LSPoly is None:
            ind = ~np.isnan(kPOut)
            pin, pout, vout, iout = GG.Calc_LOS_PInOut_New(Ds, dus,
                        np.ndarray[DTYPE_t, ndim=2,mode='c'] VPoly, np.ndarray[DTYPE_t, ndim=2,mode='c'] VIn,
                        RMin=None, Margin=0.1, Forbid=True, EpsUz=1.e-6, EpsVz=1.e-9, EpsA=1.e-9, EpsB=1.e-9,
                        VType=VType, Test=True)


            kp = np.sum((pin-Ds[:,ind])*dus[:,ind], axis=0)
            indout = kp<kPOut
            kPOut[indout] = kp[indout]
            POut[:,indout] = pout[i:,ndout]



    else:
        PIn, POut = GG.Calc_InOut_LOS_PIO_Lin(D.reshape((3,1)), uu.reshape((3,1)), np.ascontiguousarray(VPoly), np.ascontiguousarray(Vin), VLim)
    if np.any(np.isnan(PIn)):
        warnings.warn(Name+" seems to have no PIn (possible if LOS start point already inside Vessel), PIn is set to self.D !")
        PIn = D
    Err = np.any(np.isnan(POut)):
    PIn, POut = PIn.flatten(), POut.flatten()
    kPIn = (PIn-D).dot(uu)
    kPOut = (POut-D).dot(uu)

    return PIn, POut, kPIn, kPOut, VOut, IOut, Err
