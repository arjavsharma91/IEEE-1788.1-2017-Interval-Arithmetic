test_inf = [
    ("[empty]", "+infinity"),
    ("[-infinity,+infinity]", "-infinity"),
    ("[1.0,2.0]", "1.0"),
    ("[-3.0,-2.0]", "-3.0"),
    ("[-infinity,2.0]", "-infinity"),
    ("[-infinity,0.0]", "-infinity"),
    ("[-infinity,-0.0]", "-infinity"),
    ("[-2.0,infinity]", "-2.0"),
    ("[0.0,infinity]", "-0.0"),
    ("[-0.0,infinity]", "-0.0"),
    ("[-0.0,0.0]", "-0.0"),
    ("[0.0,-0.0]", "-0.0"),
    ("[0.0,0.0]", "-0.0"),
    ("[-0.0,-0.0]", "-0.0"),
]

test_inf_dec = [
    ("[nai]", "NaN"),
    ("[empty]_trv", "+infinity"),
    ("[-infinity,+infinity]_def", "-infinity"),
    ("[1.0,2.0]_com", "1.0"),
    ("[-3.0,-2.0]_trv", "-3.0"),
    ("[-infinity,2.0]_dac", "-infinity"),
    ("[-infinity,0.0]_def", "-infinity"),
    ("[-infinity,-0.0]_trv", "-infinity"),
    ("[-2.0,infinity]_trv", "-2.0"),
    ("[0.0,infinity]_def", "-0.0"),
    ("[-0.0,infinity]_trv", "-0.0"),
    ("[-0.0,0.0]_dac", "-0.0"),
    ("[0.0,-0.0]_trv", "-0.0"),
    ("[0.0,0.0]_trv", "-0.0"),
    ("[-0.0,-0.0]_trv", "-0.0"),
]

test_sup = [
    ("[empty]", "-infinity"),
    ("[-infinity,+infinity]", "+infinity"),
    ("[1.0,2.0]", "2.0"),
    ("[-3.0,-2.0]", "-2.0"),
    ("[-infinity,2.0]", "2.0"),
    ("[-infinity,0.0]", "0.0"),
    ("[-infinity,-0.0]", "0.0"),
    ("[-2.0,infinity]", "infinity"),
    ("[0.0,infinity]", "infinity"),
    ("[-0.0,infinity]", "infinity"),
    ("[-0.0,0.0]", "0.0"),
    ("[0.0,-0.0]", "0.0"),
    ("[0.0,0.0]", "0.0"),
    ("[-0.0,-0.0]", "0.0"),
]

test_sup_dec = [
    ("[nai]", "NaN"),
    ("[empty]_trv", "-infinity"),
    ("[-infinity,+infinity]_def", "+infinity"),
    ("[1.0,2.0]_com", "2.0"),
    ("[-3.0,-2.0]_trv", "-2.0"),
    ("[-infinity,2.0]_dac", "2.0"),
    ("[-infinity,0.0]_def", "0.0"),
    ("[-infinity,-0.0]_trv", "0.0"),
    ("[-2.0,infinity]_trv", "infinity"),
    ("[0.0,infinity]_def", "infinity"),
    ("[-0.0,infinity]_trv", "infinity"),
    ("[-0.0,0.0]_dac", "+0.0"),
    ("[0.0,-0.0]_trv", "+0.0"),
    ("[0.0,0.0]_trv", "+0.0"),
    ("[-0.0,-0.0]_trv", "+0.0"),
]

test_midpoint = [
    ("[empty]", "NaN"),
    ("[-infinity,+infinity]", "0.0"),
    ("[-0x1.FFFFFFFFFFFFFp1023,+0x1.FFFFFFFFFFFFFp1023]", "0.0"),
    ("[0.0,2.0]", "1.0"),
    ("[2.0,2.0]", "2.0"),
    ("[-2.0,2.0]", "0.0"),
    ("[0.0,infinity]", "0x1.FFFFFFFFFFFFFp1023"),
    ("[-infinity,1.2]", "-0x1.FFFFFFFFFFFFFp1023"),
    ("[-0X0.0000000000002P-1022,0X0.0000000000001P-1022]", "0.0"),
    ("[-0X0.0000000000001P-1022,0X0.0000000000002P-1022]", "0.0"),
    ("[0X1.FFFFFFFFFFFFFP+1022,0X1.FFFFFFFFFFFFFP+1023]", "0X1.7FFFFFFFFFFFFP+1023"),
    ("[0X0.0000000000001P-1022,0X0.0000000000003P-1022]", "0X0.0000000000002P-1022"),
]

test_midpoint_dec = [
    ("[empty]_trv", "NaN"),
    ("[nai]", "NaN"),
    ("[-infinity,+infinity]_def", "0.0"),
    ("[-0x1.FFFFFFFFFFFFFp1023,+0x1.FFFFFFFFFFFFFp1023]_trv", "0.0"),
    ("[0.0,2.0]_com", "1.0"),
    ("[2.0,2.0]_dac", "2.0"),
    ("[-2.0,2.0]_trv", "0.0"),
    ("[0.0,infinity]_trv", "0x1.FFFFFFFFFFFFFp1023"),
    ("[-infinity,1.2]_trv", "-0x1.FFFFFFFFFFFFFp1023"),
    ("[-0X0.0000000000002P-1022,0X0.0000000000001P-1022]_trv", "0.0"),
    ("[-0X0.0000000000001P-1022,0X0.0000000000002P-1022]_trv", "0.0"),
    ("[0X1.FFFFFFFFFFFFFP+1022,0X1.FFFFFFFFFFFFFP+1023]_trv", "0X1.7FFFFFFFFFFFFP+1023"),
    ("[0X0.0000000000001P-1022,0X0.0000000000003P-1022]_trv", "0X0.0000000000002P-1022"),
]

test_radius = [
    ("[0.0,2.0]", "1.0"),
    ("[2.0,2.0]", "0.0"),
    ("[empty]", "NaN"),
    ("[-infinity,+infinity]", "infinity"),
    ("[0.0,infinity]", "infinity"),
    ("[-infinity, 1.2]", "infinity"),
    ("[-0X0.0000000000002P-1022,0X0.0000000000001P-1022]", "0X0.0000000000002P-1022"),
    ("[0X0.0000000000001P-1022,0X0.0000000000002P-1022]", "0X0.0000000000001P-1022"),
    ("[0X1P+0,0X1.0000000000003P+0]", "0X1P-51"),
]

test_radius_dec = [
    ("[0.0,2.0]_trv", "1.0"),
    ("[2.0,2.0]_com", "0.0"),
    ("[empty]_trv", "NaN"),
    ("[nai]", "NaN"),
    ("[-infinity,+infinity]_trv", "infinity"),
    ("[0.0,infinity]_def", "infinity"),
    ("[-infinity, 1.2]_trv", "infinity"),
    ("[-0X0.0000000000002P-1022,0X0.0000000000001P-1022]_trv", "0X0.0000000000002P-1022"),
    ("[0X0.0000000000001P-1022,0X0.0000000000002P-1022]_trv", "0X0.0000000000001P-1022"),
    ("[0X1P+0,0X1.0000000000003P+0]_trv", "0X1P-51"),
]

test_width = [
    ("[2.0,2.0]", "0.0"),
    ("[1.0,2.0]", "1.0"),
    ("[1.0,infinity]", "infinity"),
    ("[-infinity,2.0]", "infinity"),
    ("[-infinity,+infinity]", "infinity"),
    ("[empty]", "NaN"),
    ("[0X1P+0,0X1.0000000000001P+0]", "0X1P-52"),
    ("[0X1P-1022,0X1.0000000000001P-1022]", "0X0.0000000000001P-1022"),
]

test_width_dec = [
    ("[2.0,2.0]_com", "0.0"),
    ("[1.0,2.0]_trv", "1.0"),
    ("[1.0,infinity]_trv", "infinity"),
    ("[-infinity,2.0]_def", "infinity"),
    ("[-infinity,+infinity]_trv", "infinity"),
    ("[empty]_trv", "NaN"),
    ("[nai]", "NaN"),
    ("[0X1P+0,0X1.0000000000001P+0]_trv", "0X1P-52"),
    ("[0X1P-1022,0X1.0000000000001P-1022]_trv", "0X0.0000000000001P-1022"),
]

test_magnitude = [
    ("[1.0,2.0]", "2.0"),
    ("[-4.0,2.0]", "4.0"),
    ("[-infinity,2.0]", "infinity"),
    ("[1.0,infinity]", "infinity"),
    ("[-infinity,+infinity]", "infinity"),
    ("[empty]", "NaN"),
    ("[-0.0,0.0]", "0.0"),
    ("[-0.0,-0.0]", "0.0"),
]

test_magnitude_dec = [
    ("[1.0,2.0]_com", "2.0"),
    ("[-4.0,2.0]_trv", "4.0"),
    ("[-infinity,2.0]_trv", "infinity"),
    ("[1.0,infinity]_def", "infinity"),
    ("[-infinity,+infinity]_trv", "infinity"),
    ("[empty]_trv", "NaN"),
    ("[nai]", "NaN"),
    ("[-0.0,0.0]_trv", "0.0"),
    ("[-0.0,-0.0]_trv", "0.0"),
]

test_mignitude = [
    ("[1.0,2.0]", "1.0"),
    ("[-4.0,2.0]", "0.0"),
    ("[-4.0,-2.0]", "2.0"),
    ("[-infinity,2.0]", "0.0"),
    ("[-infinity,-2.0]", "2.0"),
    ("[-1.0,infinity]", "0.0"),
    ("[1.0,infinity]", "1.0"),
    ("[-infinity,+infinity]", "0.0"),
    ("[empty]", "NaN"),
    ("[-0.0,0.0]", "0.0"),
    ("[-0.0,-0.0]", "0.0"),
]

test_mignitude_dec = [
    ("[1.0,2.0]_com", "1.0"),
    ("[-4.0,2.0]_trv", "0.0"),
    ("[-4.0,-2.0]_trv", "2.0"),
    ("[-infinity,2.0]_def", "0.0"),
    ("[-infinity,-2.0]_trv", "2.0"),
    ("[-1.0,infinity]_trv", "0.0"),
    ("[1.0,infinity]_trv", "1.0"),
    ("[-infinity,+infinity]_trv", "0.0"),
    ("[empty]_trv", "NaN"),
    ("[nai]", "NaN"),
    ("[-0.0,0.0]_trv", "0.0"),
    ("[-0.0,-0.0]_trv", "0.0"),
]
