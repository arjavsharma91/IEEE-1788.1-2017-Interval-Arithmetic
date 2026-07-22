test_sinh = [
    ("[empty]", "[empty]"),
    ("[0.0,infinity]", "[0.0,infinity]"),
    ("[-0.0,infinity]", "[0.0,infinity]"),
    ("[-infinity,0.0]", "[-infinity,0.0]"),
    ("[-infinity,-0.0]", "[-infinity,0.0]"),
    ("[entire]", "[entire]"),
    ("[0.0,0.0]", "[0.0,0.0]"),
    ("[-0.0,-0.0]", "[0.0,0.0]"),
    ("[1.0,0X1.2C903022DD7AAP+8]", "[0X1.2CD9FC44EB982P+0,0X1.89BCA168970C6P+432]"),
    ("[-0X1.FD219490EAAC1P+38,-0X1.1AF1C9D74F06DP+9]", "[-infinity,-0X1.53045B4F849DEP+815]"),
    ("[-0X1.199999999999AP+0,0X1.2666666666666P+1]", "[-0X1.55ECFE1B2B215P+0,0X1.3BF72EA61AF1BP+2]"),
]

test_sinh_dec = [
    ("[entire]_dac", "[entire]_dac"),
    ("[0.0,infinity]_dac", "[0.0,infinity]_dac"),
    ("[-infinity,0.0]_def", "[-infinity,0.0]_def"),
    ("[1.0,0X1.2C903022DD7AAP+8]_com", "[0X1.2CD9FC44EB982P+0,0X1.89BCA168970C6P+432]_com"),
    ("[-0X1.FD219490EAAC1P+38,-0X1.1AF1C9D74F06DP+9]_com", "[-infinity,-0X1.53045B4F849DEP+815]_dac"),
]

test_cosh = [
    ("[empty]", "[empty]"),
    ("[0.0,infinity]", "[1.0,infinity]"),
    ("[-0.0,infinity]", "[1.0,infinity]"),
    ("[-infinity,0.0]", "[1.0,infinity]"),
    ("[-infinity,-0.0]", "[1.0,infinity]"),
    ("[entire]", "[1.0,infinity]"),
    ("[0.0,0.0]", "[1.0,1.0]"),
    ("[-0.0,-0.0]", "[1.0,1.0]"),
    ("[1.0,0X1.2C903022DD7AAP+8]", "[0X1.8B07551D9F55P+0,0X1.89BCA168970C6P+432]"),
    ("[-0X1.FD219490EAAC1P+38,-0X1.1AF1C9D74F06DP+9]", "[0X1.53045B4F849DEP+815,infinity]"),
    ("[-0X1.199999999999AP+0,0X1.2666666666666P+1]", "[1.0,0X1.4261D2B7D6181P+2]"),
]

test_cosh_dec = [
    ("[0.0,infinity]_dac", "[1.0,infinity]_dac"),
    ("[-infinity,0.0]_def", "[1.0,infinity]_def"),
    ("[entire]_def", "[1.0,infinity]_def"),
    ("[1.0,0X1.2C903022DD7AAP+8]_def", "[0X1.8B07551D9F55P+0,0X1.89BCA168970C6P+432]_def"),
    ("[-0X1.FD219490EAAC1P+38,-0X1.1AF1C9D74F06DP+9]_com", "[0X1.53045B4F849DEP+815,infinity]_dac"),
]

test_tanh = [
    ("[empty]", "[empty]"),
    ("[0.0,infinity]", "[0.0,1.0]"),
    ("[-0.0,infinity]", "[0.0,1.0]"),
    ("[-infinity,0.0]", "[-1.0,0.0]"),
    ("[-infinity,-0.0]", "[-1.0,0.0]"),
    ("[entire]", "[-1.0,1.0]"),
    ("[0.0,0.0]", "[0.0,0.0]"),
    ("[-0.0,-0.0]", "[0.0,0.0]"),
    ("[1.0,0X1.2C903022DD7AAP+8]", "[0X1.85EFAB514F394P-1,0X1P+0]"),
    ("[-0X1.FD219490EAAC1P+38,-0X1.1AF1C9D74F06DP+9]", "[-0X1P+0,-0X1.FFFFFFFFFFFFFP-1]"),
    ("[-0X1.199999999999AP+0,0X1.2666666666666P+1]", "[-0X1.99DB01FDE2406P-1,0X1.F5CF31E1C8103P-1]"),
]

test_tanh_dec = [
    ("[0.0,infinity]_dac", "[0.0,1.0]_dac"),
    ("[-infinity,0.0]_def", "[-1.0,0.0]_def"),
    ("[entire]_dac", "[-1.0,1.0]_dac"),
    ("[1.0,0X1.2C903022DD7AAP+8]_com", "[0X1.85EFAB514F394P-1,0X1P+0]_com"),
    ("[-0X1.FD219490EAAC1P+38,-0X1.1AF1C9D74F06DP+9]_trv", "[-0X1P+0,-0X1.FFFFFFFFFFFFFP-1]_trv"),
]

test_asinh = [
    ("[empty]", "[empty]"),
    ("[0.0,infinity]", "[0.0,infinity]"),
    ("[-0.0,infinity]", "[0.0,infinity]"),
    ("[-infinity,0.0]", "[-infinity,0.0]"),
    ("[-infinity,-0.0]", "[-infinity,0.0]"),
    ("[entire]", "[entire]"),
    ("[0.0,0.0]", "[0.0,0.0]"),
    ("[-0.0,-0.0]", "[0.0,0.0]"),
    ("[1.0,0X1.2C903022DD7AAP+8]", "[0X1.C34366179D426P-1,0X1.9986127438A87P+2]"),
    ("[-0X1.FD219490EAAC1P+38,-0X1.1AF1C9D74F06DP+9]", "[-0X1.BB86380A6CC45P+4,-0X1.C204D8EB20827P+2]"),
    ("[-0X1.199999999999AP+0,0X1.2666666666666P+1]", "[-0X1.E693DF6EDF1E7P-1,0X1.91FDC64DE0E51P+0]"),
]

test_asinh_dec = [
    ("[0.0,infinity]_dac", "[0.0,infinity]_dac"),
    ("[-infinity,0.0]_trv", "[-infinity,0.0]_trv"),
    ("[entire]_dac", "[entire]_dac"),
    ("[1.0,0X1.2C903022DD7AAP+8]_com", "[0X1.C34366179D426P-1,0X1.9986127438A87P+2]_com"),
    ("[-0X1.FD219490EAAC1P+38,-0X1.1AF1C9D74F06DP+9]_def", "[-0X1.BB86380A6CC45P+4,-0X1.C204D8EB20827P+2]_def"),
]

test_acosh = [
    ("[empty]", "[empty]"),
    ("[0.0,infinity]", "[0.0,infinity]"),
    ("[-0.0,infinity]", "[0.0,infinity]"),
    ("[1.0,infinity]", "[0.0,infinity]"),
    ("[-infinity,1.0]", "[0.0,0.0]"),
    ("[-infinity,0X1.FFFFFFFFFFFFFP-1]", "[empty]"),
    ("[entire]", "[0.0,infinity]"),
    ("[1.0,1.0]", "[0.0,0.0]"),
    ("[1.0,0X1.2C903022DD7AAP+8]", "[0.0,0X1.9985FB3D532AFP+2]"),
    ("[0X1.199999999999AP+0,0X1.2666666666666P+1]", "[0X1.C636C1A882F2CP-2,0X1.799C88E79140DP+0]"),
    ("[0X1.14D4E82B2B26FP+15,0X1.72DBE91C837B5P+29]", "[0X1.656510B4BAEC3P+3,0X1.52A415EE8455AP+4]"),
]

test_acosh_dec = [
    ("[0.0,infinity]_dac", "[0.0,infinity]_trv"),
    ("[1.0,infinity]_dac", "[0.0,infinity]_dac"),
    ("[entire]_dac", "[0.0,infinity]_trv"),
    ("[1.0,1.0]_com", "[0.0,0.0]_com"),
    ("[0.9,1.0]_com", "[0.0,0.0]_trv"),
    ("[1.0,0X1.2C903022DD7AAP+8]_dac", "[0.0,0X1.9985FB3D532AFP+2]_dac"),
    ("[0.9,0X1.2C903022DD7AAP+8]_com", "[0.0,0X1.9985FB3D532AFP+2]_trv"),
    ("[0X1.14D4E82B2B26FP+15,0X1.72DBE91C837B5P+29]_def", "[0X1.656510B4BAEC3P+3,0X1.52A415EE8455AP+4]_def"),
]

test_atanh = [
    ("[empty]", "[empty]"),
    ("[0.0,infinity]", "[0.0,infinity]"),
    ("[-0.0,infinity]", "[0.0,infinity]"),
    ("[1.0,infinity]", "[empty]"),
    ("[-infinity,0.0]", "[-infinity,0.0]"),
    ("[-infinity,-0.0]", "[-infinity,0.0]"),
    ("[-infinity,-1.0]", "[empty]"),
    ("[-1.0,1.0]", "[entire]"),
    ("[0.0,0.0]", "[0.0,0.0]"),
    ("[-0.0,-0.0]", "[0.0,0.0]"),
    ("[-1.0,-1.0]", "[empty]"),
    ("[1.0,1.0]", "[empty]"),
    ("[entire]", "[entire]"),
    ("[0X1.4C0420F6F08CCP-2,0X1.FFFFFFFFFFFFFP-1]", "[0X1.5871DD2DF9102P-2,0X1.2B708872320E2P+4]"),
    ("[-0X1.FFB88E9EB6307P-1,0X1.999999999999AP-4]", "[-0X1.06A3A97D7979CP+2,0X1.9AF93CD234413P-4]"),
]

test_atanh_dec = [
    ("[0.0,infinity]_dac", "[0.0,infinity]_trv"),
    ("[-infinity,0.0]_def", "[-infinity,0.0]_trv"),
    ("[-1.0,1.0]_com", "[entire]_trv"),
    ("[0.0,0.0]_com", "[0.0,0.0]_com"),
    ("[1.0,1.0]_def", "[empty]_trv"),
    ("[0X1.4C0420F6F08CCP-2,0X1.FFFFFFFFFFFFFP-1]_com", "[0X1.5871DD2DF9102P-2,0X1.2B708872320E2P+4]_com"),
    ("[-1.0,0X1.FFFFFFFFFFFFFP-1]_com", "[-infinity,0X1.2B708872320E2P+4]_trv"),
    ("[-0X1.FFB88E9EB6307P-1,0X1.999999999999AP-4]_def", "[-0X1.06A3A97D7979CP+2,0X1.9AF93CD234413P-4]_def"),
    ("[-0X1.FFB88E9EB6307P-1,1.0]_com", "[-0X1.06A3A97D7979CP+2,infinity]_trv"),
]
