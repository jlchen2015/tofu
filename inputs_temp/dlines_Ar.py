

_DSOURCES = {
    'Kallne': ('Kallne et al., '
               + 'High Resolution X-Ray Spectroscopy Diagnostics'
               + ' of High Temperature Plasmas'
               + ', Physica Scripta, vol. 31, 6, pp. 551-564, 1985')
    'Bitter': ('Bitter et al., '
               + 'XRay diagnostics of tokamak plasmas'
               + ', Physica Scripta, vol. 47, pp. 87-95, 1993')
}

dlines = {
    # --------------------------
    # Ar
    # --------------------------

    'ArXV_1': {'Z': 18, 'q': 14, 'element': 'Ar', 'ION': 'ArXV',
               'symbol': '1', 'lambda': 4.0096e-10,
               'transition': [r'$1s2s^22p(^1P_1)$', r'$1s^22s^2(^1S_0)$'],
               'source': 'Kallne', 'innershell': True},
    'ArXV_2-1': {'Z': 18, 'q': 14, 'element': 'Ar', 'ION': 'ArXV',
                 'symbol': '2-1', 'lambda': 4.0176e-10,
                 'transition': [r'$1s2p^22s(^4P^3P_1)$', r'$1s^22s2p(^3P_1)$'],
                 'source': 'Kallne'},
    'ArXV_2-2': {'Z': 18, 'q': 14, 'element': 'Ar', 'ION': 'ArXV',
                 'symbol': '2-2', 'lambda': 4.0179e-10,
                 'transition': [r'$1s2s2p^2(^3D_1)$', r'$1s^22s2p(^3P_0)$'],
                 'source': 'Kallne'},
    'ArXV_2-3': {'Z': 18, 'q': 14, 'element': 'Ar', 'ION': 'ArXV',
                 'symbol': '2-3', 'lambda': 4.0180e-10,
                 'transition': [r'$1s2p^22s(^4P^3P_2)$', r'$1s^22s2p(^3P_2)$'],
                 'source': 'Kallne'},
    'ArXV_3': {'Z': 18, 'q': 14, 'element': 'Ar', 'ION': 'ArXV',
               'symbol': '3', 'lambda': 4.0192e-10,
               'transition': [r'$1s2s2p^2(^3D_2)$', r'$1s^22s2p(^3P_1)$'],
               'source': 'Kallne'},
    'ArXV_4': {'Z': 18, 'q': 14, 'element': 'Ar', 'ION': 'ArXV',
               'symbol': '4', 'lambda': 4.0219e-10,
               'transition': [r'$1s2s2p^2(^3D_5)$', r'$1s^22s2p(^3P_2)$'],
               'source': 'Kallne'},
    'ArXV_5': {'Z': 18, 'q': 14, 'element': 'Ar', 'ION': 'ArXV',
               'symbol': '5', 'lambda': 4.0291e-10,
               'transition': [r'$1s2s2p^2(^1D_5)$', r'$1s^22s2p(^1P_1)$'],
               'source': 'Kallne'},

    'ArXVI_m': {'Z': 18, 'q': 15, 'element': 'Ar', 'ION': 'ArXVI',
                'symbol': 'm', 'lambda': 3.9562e-10,
                'transition': [r'$1s2p^2(^2S_{1/2})$', r'$1s^22p(^2P_{3/2})$'],
                'source': 'Kallne'},
    'ArXVI_s': {'Z': 18, 'q': 15, 'element': 'Ar', 'ION': 'ArXVI',
                'symbol': 's', 'lambda': 3.9669e-10,
                'transition': [r'$1s2s2p(^1P)^2P_{3/2}$', r'$1s^22s(^2S_{1/2})$'],
                'source': 'Kallne'},
    'ArXVI_t': {'Z': 18, 'q': 15, 'element': 'Ar', 'ION': 'ArXVI',
                'symbol': 't', 'lambda': 3.9677e-10,
                'transition': [r'$1s2s2p(^1P)^2P_{1/2}$', r'$1s^22s(^2S_{1/2})$'],
                'source': 'Kallne'},
    'ArXVI_q': {'Z': 18, 'q': 15, 'element': 'Ar', 'ION': 'ArXVI',
                'symbol': 'q', 'lambda': 3.9806e-10,
                'transition': [r'$1s2s2p(^1P)^2P_{3/2}$', r'$1s^22s(^2S_{1/2})$'],
                'source': 'Kallne', 'innershell': True},
    'ArXVI_r': {'Z': 18, 'q': 15, 'element': 'Ar', 'ION': 'ArXVI',
                'symbol': 'r', 'lambda': 3.9827e-10,
                'transition': [r'$1s2s2p(^1P)^2P_{1/2}$', r'$1s^22s(^2S_{1/2})$'],
                'source': 'Kallne'},
    'ArXVI_a': {'Z': 18, 'q': 15, 'element': 'Ar', 'ION': 'ArXVI',
                'symbol': 'a', 'lambda': 3.9852e-10,
                'transition': [r'$1s2p^2(^2P_{3/2})$', r'$1s^22p(^2P_{1/2})$'],
                'source': 'Kallne'},
    'ArXVI_k': {'Z': 18, 'q': 15, 'element': 'Ar', 'ION': 'ArXVI',
                'symbol': 'k', 'lambda': 3.9892e-10,
                'transition': [r'$1s2p^2(^2D_{3/2})$', r'$1s^22p(^2P_{1/2})$'],
                'source': 'Kallne', 'comment': 'Dielect. recomb. from ArXVII'},
    'ArXVI_j': {'Z': 18, 'q': 15, 'element': 'Ar', 'ION': 'ArXVI',
                'symbol': 'j', 'lambda': 3.9932e-10,
                'transition': [r'$1s2p^2(^2D_{5/2})$', r'$1s^22p(^2P_{3/2})$'],
                'source': 'Kallne'},

    'ArXVII_w': {'Z': 18, 'q': 16, 'element': 'Ar', 'ION': 'ArXVII',
                 'symbol': 'w', 'lambda': 3.9482e-10,
                 'transition': [r'$1s2p(^1P_1)$', r'$1s^2(^1S_0)$'],
                 'source': 'Kallne'},
    'ArXVII_x': {'Z': 18, 'q': 16, 'element': 'Ar', 'ION': 'ArXVII',
                 'symbol': 'x', 'lambda': 3.9649e-10,
                 'transition': [r'$1s2p(^3P_2)$', r'$1s^2(^1S_0)$'],
                 'source': 'Kallne'},
    'ArXVII_y': {'Z': 18, 'q': 16, 'element': 'Ar', 'ION': 'ArXVII',
                 'symbol': 'y', 'lambda': 3.9683e-10,
                 'transition': [r'$1s2p(^3P_1)$', r'$1s^2(^1S_0)$'],
                 'source': 'Kallne'},
    'ArXVII_z': {'Z': 18, 'q': 16, 'element': 'Ar', 'ION': 'ArXVII',
                 'symbol': 'z', 'lambda': 3.9934e-10,
                 'transition': [r'$1s2s(^3S_1)$', r'$1s^2(^1S_0)$'],
                 'source': 'Kallne'},

    'ArXVIII_W1': {'Z': 18, 'q': 17, 'element': 'Ar', 'ION': 'ArXVIII',
                   'symbol': 'W_1', 'lambda': 3.7300e-10,
                   'transition': [r'$2p(^2P_{3/2})$', r'$1s(^2S_{1/2})$'],
                   'source': 'Kallne'},
    'ArXVIII_W2': {'Z': 18, 'q': 17, 'element': 'Ar', 'ION': 'ArXVIII',
                   'symbol': 'W_2', 'lambda': 3.7352e-10,
                   'transition': [r'$2p(^2P_{1/2})$', r'$1s(^2S_{1/2})$'],
                   'source': 'Kallne'},

    'ArXVII_T': {'Z': 18, 'q': 16, 'element': 'Ar', 'ION': 'ArXVII',
                 'symbol': 'T', 'lambda': 3.7544e-10,
                 'transition': [r'$2s2p(^1P_1)$', r'$1s2s(^1S_0)$'],
                 'source': 'Kallne'},
    'ArXVII_K': {'Z': 18, 'q': 16, 'element': 'Ar', 'ION': 'ArXVII',
                 'symbol': 'K', 'lambda': 3.7557e-10,
                 'transition': [r'$2p^2(^1D_2)$', r'$1s2p(^3P_2)$'],
                 'source': 'Kallne'},
    'ArXVII_Q': {'Z': 18, 'q': 16, 'element': 'Ar', 'ION': 'ArXVII',
                 'symbol': 'Q', 'lambda': 3.7603e-10,
                 'transition': [r'$2s2p(^3P_2)$', r'$1s2s(^3S_1)$'],
                 'source': 'Kallne'},
    'ArXVII_B': {'Z': 18, 'q': 16, 'element': 'Ar', 'ION': 'ArXVII',
                 'symbol': 'B', 'lambda': 3.7626e-10,
                 'transition': [r'$2p^2(^3P_2)$', r'$1s2p(^3P_1)$'],
                 'source': 'Kallne'},
    'ArXVII_R': {'Z': 18, 'q': 16, 'element': 'Ar', 'ION': 'ArXVII',
                 'symbol': 'R', 'lambda': 3.7639e-10,
                 'transition': [r'$2s2p(^3P_1)$', r'$1s2s(^3S_1)$'],
                 'source': 'Kallne'},
    'ArXVII_A': {'Z': 18, 'q': 16, 'element': 'Ar', 'ION': 'ArXVII',
                 'symbol': 'A', 'lambda': 3.7657e-10,
                 'transition': [r'$2p^2(^3P_2)$', r'$1s2p(^3P_2)$'],
                 'source': 'Kallne'},
    'ArXVII_J': {'Z': 18, 'q': 16, 'element': 'Ar', 'ION': 'ArXVII',
                 'symbol': 'J', 'lambda': 3.7709e-10,
                 'transition': [r'$2p^2(^1D_2)$', r'$1s2p(^1P_1)$'],
                 'source': 'Kallne'}

    # --------------------------
    # Fe
    # --------------------------

    'FeXXV_w': {'Z': 26, 'q': 24, 'element': 'Fe', 'ION': 'FeXXV',
                'symbol': 'w', 'lambda': 1.8498e-10,
                'transition': [r'$1s2p(^1P_1)$', r'$1s^2(^1S_0)$'],
                'source': 'Bitter'},
    'FeXXV_x': {'Z': 26, 'q': 24, 'element': 'Fe', 'ION': 'FeXXV',
                'symbol': 'x', 'lambda': 1.85503e-10,
                'transition': [r'$1s2p(^3P_2)$', r'$1s^2(^1S_0)$'],
                'source': 'Bitter'},
    'FeXXV_y': {'Z': 26, 'q': 24, 'element': 'Fe', 'ION': 'FeXXV',
                'symbol': 'y', 'lambda': 1.8590e-10,
                'transition': [r'$1s2p(^3P_1)$', r'$1s^2(^1S_0)$'],
                'source': 'Bitter'},

    # TBC !!!
    'FeXXV_k': {'Z': 26, 'q': 24, 'element': 'Fe', 'ION': 'FeXXV',
                'symbol': 'k', 'lambda': 1.8626e-10,
                'transition': [r'$1s2p(^3P_1)$', r'$1s^2(^1S_0)$'],
                'source': 'Bitter'},

    'FeXXIII_t': {'Z': 26, 'q': 22, 'element': 'Fe', 'ION': 'FeXXIII',
                'symbol': 't', 'lambda': 1.8566e-10,
                'transition': [r'$1s2s2p(^1P^2P_{1/2})$', r'$1s^22s^2(S_{1/2})$'],
                'source': 'Bitter'},
    'FeXXIII_q': {'Z': 26, 'q': 22, 'element': 'Fe', 'ION': 'FeXXIII',
                'symbol': 'q', 'lambda': 1.8605e-10,
                'transition': [r'$1s2s2p(^3P^2P_{3/2})$',
                               r'$1s^22s^2(S_{1/2})$'],  # TBC (2s2s vs 2s2p)
                'source': 'Bitter'},





}
