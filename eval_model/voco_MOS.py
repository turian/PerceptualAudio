import numpy
import numpy as np

def voco_mos(final_pesq):
    
    mos_SLT = np.array([
      [2.7273,2.9091,2.875,4.1429,3.3,4.875],
      [3.4444,3.8571,4.4,4.8333,4.4444,5],
      [3.6667,4,4.3,4.6667,4.3333,4.9091],
      [2.25,3.9,4,4.6667,4.5714,5],
      [3.1111,2.875,2.8571,4.0833,4.4444,4.8],
      [2.7,2.4444,4.75,4,4.7778,5],
      [3.5556,4,4.3636,3.625,4.1429,5],
      [1.8571,3.6,3.1667,3.6,4.125,5],
      [1.75,1.9,3.6667,4,3.6,4.9167],
      [2.8889,3.25,3.0833,3.5,3.8889,4.7778],
      [2,4.1429,3,4.6667,4.1111,4.75],
      [2.6364,3.2222,2.125,4.1111,4.2,4.5],
      [1.5,4.25,4.8333,4.6,5,4.6],
      [2.6667,3.4444,4.4,3.8,3.75,4.125],
      [4,4.9091,4.8,4.4444,4.7778,4.625],
      [3.6667,3.25,2.625,3,4.4286,4.4444],
      [2,3.375,3.6,4,4,4.6667],
      [2.4167,3.8571,4.25,4.4,4.25,4.7143],
      [1.8333,3.4,4.25,3.7143,4.6,4.7778],
      [1.8571,4.625,4.1,4.0909,4.1667,4.875],
      [3.625,3.3333,3.875,4.4,5,5],
      [2.7273,4.3636,3.8571,4.6667,4.375,4.6],
      [3.25,2.6667,4.2857,4.4,4.5,4.875],
      [3.6667,3.7143,4.7143,3.75,4.3333,4.6364],
      [2.4545,4,3.875,3.7273,3.6,4.6364],
      [2.7143,3.375,3.5,4.4,4.2222,4.75],
      [2.8333,4.7143,4.4,4.1667,4.6364,4.6667],
      [3.8333,4.2222,4.7778,4,4,4.9],
      [2.7778,3,3.5714,4.25,4.1111,4.8333],
      [3.75,3.875,4.3,3.2,4.2,5],
      [3.1429,2.5,3.8182,5,4.7778,5],
      [3.4444,3.7778,4.1429,5,4.7778,4.875],
      [2.75,2.2857,4,4.2222,3.625,5],
      [3.2,2.375,4.5556,4.6,3.8333,4.875],
      [3,2,3.1111,3.5,3.4286,4.7],
      [2,4,2.4444,3.7143,4.3333,5],
      [3.5714,3.75,4.6667,4.7778,4.8571,4.75],
      [3.5714,4.8571,4.2857,4.375,4.7778,4.8182],
      [4,2.8,4.75,4.1818,4.7778,5],
      [2.5556,3.2857,3.375,4.5455,4.7,4.8],
      [3.25,2.375,5,4.8889,4.3636,4.8],
      [2.7273,2.4,4.3333,4.2857,4.5,4.8571],
      [2.1818,3.375,4.4,4.8,4.7,4.875],
      [2.4,4.4286,4.25,4.625,4.875,4.5556]
    ])

    mos_CLB = np.array([
      [2.1111,2.4286,3.6667,4.4444,3.4444,4.75],
      [2.4286,4.4545,5,4.8,4.8333,5],
      [1.5,4.2222,4.625,4.5833,4.125,5],
      [2,4.9,4.7143,4.8,4.6667,4.6667],
      [1.8889,2.2,4.375,4.2,4.2222,4.3333],
      [1.5714,3,4.8182,4.25,4.8889,4.5],
      [2.8333,4,3.375,3.3333,4,4.6667],
      [1.25,4.9,4.6,4.9091,4.8889,4.8333],
      [2.125,2.25,3.4,3.5714,3.75,4.8333],
      [1.5556,3.8,3.375,4.2,4.5556,4.875],
      [1.3333,3.3333,4.1818,4.4444,3.8889,4.8889],
      [2.9,4.5714,3.8571,4.25,4.5833,5],
      [2.5,2.625,4.5,4.5,4.625,4.6],
      [1.2857,2.4444,3.5833,3.8889,4.7273,4.875],
      [2.8889,4.75,4.8,4.8,4.9091,5],
      [2.2222,4,4.5556,4.6,4.6667,4.9],
      [1.6667,4.6667,4.4286,4.625,4.625,4.9],
      [1.75,4.8571,4.8,4.75,5,4.875],
      [1.3333,3.625,4.75,4.8,4.4,5],
      [1.7143,3.1429,4.1111,4,3.7778,4.5556],
      [1.3333,3.5,4,4.9,4.2857,4.9],
      [1.4444,4.8889,4.8182,4.8333,4.5556,5],
      [2.5,3.7778,4.8571,4.5556,4.8571,4.9],
      [2.5,2.7,4.25,3.875,4,4.75],
      [1.6364,4.1667,4.3333,4.5,4.1667,5],
      [1.625,3.4,3.6364,4.5556,4.0909,5],
      [1.8,4.7143,4.7143,5,4.3333,4.9091],
      [2.1429,4.3636,4.4,3.75,4.3,4.5556],
      [2.5556,4.4545,4.6667,4.1818,4.1429,4.8889],
      [2.2857,3.4,4.1,4.5556,4.7,4.8],
      [1.875,3.1,3.8889,4.875,5,5],
      [2.3333,4.6,4.5714,5,5,4.7273],
      [2,4.1111,3.9,4.5,3.8333,4.875],
      [2,4.2857,4.4,4.8333,4.5714,5],
      [1.5,2.4286,4,3.7143,3.8333,4.8182],
      [1.8571,4,4.125,3.8182,4,5],
      [2,4.1111,4.1818,4.875,4.7778,4.75],
      [2.1429,4.875,5,4.8571,5,5],
      [2.25,4.8571,4.75,3.5,4.75,4.6667],
      [1.8571,3.8889,4.5,4.2,4.6,4.7778],
      [1.9,4.6,3.5714,4.4,4.5,4.7],
      [1.6667,4.3,4.5714,4,4.5,4.8889],
      [1.625,4.3333,4.125,3.9,4.125,5],
      [2.2,4,4.3,4.25,4.4444,4.875],
    ])

    mos_RMS = np.array([
      [2.8889,3.5,4,3.9,3.625,4.8571],
      [2.5,4.25,4.625,4.8333,4.5714,4.4],
      [2.6,3.9091,4.4444,3.2857,4,5],
      [1.9091,4.5714,4.6667,4.5556,4.7143,4.3333],
      [2.7778,3,3.1667,4.1,4.5,4.5],
      [2.6667,3,4.4,3.6667,4.2857,5],
      [2.6,4.4444,4,4.125,5,4.8],
      [2.125,4.5714,4.3636,4.8571,4.5833,4],
      [2.7143,3.875,4.75,4.2857,4.3333,4.8],
      [2.1111,4,3.4545,4.25,4.25,4.7778],
      [2.4,3,4.5,4.2222,4.7,4.2857],
      [2.8333,2.4,2.75,4.1111,4.375,4.7778],
      [2.5,2.6667,4.375,4.5,4.7778,4.4],
      [2.4286,2.6667,3.125,3.5714,4.5,4.25],
      [2.1111,4.7143,4.7273,4.6667,4.8333,5],
      [2.875,3.8182,4.75,4.6667,4.6667,4.7273],
      [3,4.7143,4.875,4.4286,4,4.9091],
      [2.6,3,4.2857,4.7143,4.6667,4.3333],
      [2,4.3,4.2,4.2,4.6,4.2857],
      [3.125,4.1429,4.4,3.6667,2.875,4.7],
      [2.2727,4,5,4.1429,4.7143,4.75],
      [2.8571,4.7778,4.5,4.75,4.6667,4.75],
      [2.6667,4.5,4.6667,4,4.7273,4.625],
      [3.8571,3.2,4.1818,3.7,4,4],
      [2.6667,4,4.3333,4.0909,4.1667,4.7778],
      [2.1111,3.6667,4,3.625,4,5],
      [1.5714,4.6667,4.3333,4.375,4.375,4.5556],
      [4.5,3.9,4.8,4.6667,4.4545,4.75],
      [2.1429,4,4.125,4.1429,4.4286,4.4545],
      [2.2222,3.5,3.9,4.8571,4.6,5],
      [2.1667,4.25,3.8889,4.375,4.4545,4.8889],
      [3,4.5,4.7273,4.7778,4.7143,4.6],
      [1.6667,2.1429,4.5,4.7,4.7,4.5556],
      [2.8889,3.2,4.1,4.75,4.6667,4.6667],
      [2.625,3.4286,3.8333,4.1,4.3333,4.7143],
      [1.9,4.3,4.5,3.625,5,4.4286],
      [2.625,4.8889,4.3636,4.4286,4.25,4.3333],
      [4.125,5,5,4.1429,4.875,4.75],
      [2.1429,4.1429,4.4,4.7273,4.8,4.75],
      [2.6,3.8333,4.6667,4.0769,4.4,5],
      [3.0909,4.4286,4.7143,4.8333,4.4286,4.5556],
      [2.625,4.25,4.75,4.5,4.6667,4.5556],
      [2.125,4,4,4,4.5,4.7778],
      [2.1,3.2,4.3333,4.6,4.5,4.75],
    ])

    mos_DBL = np.array([
      [3.1111,2.9091,2.875,3.4444,3.75,4.5556],
      [1.4444,4.25,4.4286,4.3333,4.8,4.6667],
      [2.2222,4.0769,5,5,5,5],
      [1.25,4.8333,4.5,4.4,4.4167,5],
      [1.7143,3.7778,4.125,4.3,4.875,4.7778],
      [1.8182,3.1429,4.8,4.375,4.6,4.8571],
      [1.6667,3.1667,4,4.2222,3.4286,4.625],
      [1.2,4.1111,5,5,4.625,4.6667],
      [1.4444,3.625,4.25,3.1667,4.1667,4.9],
      [1.8,4.875,4.8462,4.4286,4.7143,4.9],
      [1.9,4.2857,2.75,3.6667,4.4444,4.8333],
      [1.6667,4.5,4,4.1111,4.2222,4.7778],
      [2.5,4.6667,4.5,4.3333,4.2222,4.7778],
      [1.6667,3.4545,3.6,3.6667,4.5,4.75],
      [1.9,4.5,4.6,5,4.875,4.7778],
      [1.9,4.8333,4.4444,4.25,3.7143,4.6],
      [1.9091,3,4.125,4,4.375,4.375],
      [1.5,1.875,2.375,4,3.8333,4.7],
      [1.2,4,3.5714,4.3333,4,4.9],
      [1.7778,3.4444,3.5,4.2727,4.7143,4.7143],
      [1.5833,3.7778,4.8571,4.6,4.625,4.7778],
      [1.6667,4.5455,4,4.5,4.125,4.7143],
      [1.4,3.4167,4.2222,5,4.5,4.6667],
      [1.4444,2.5,4.2,3,4.1,4.75],
      [1.6667,3.6667,4,3.6667,4.7143,4.5556],
      [1.8,3,3.1818,3.2222,4.6,4.8889],
      [1.3333,4.8889,4.2222,4.4444,4.4286,4.8571],
      [2,3.9,4.2857,5,4.1429,5],
      [2.2857,4.1111,3.2,4.2727,4.6667,4.8182],
      [2.625,2.8333,4,4,4.25,4.7778],
      [1.8,4.625,3.4286,4.125,3.8571,4.5556],
      [2.5,3,4.75,4.8889,4.6667,4.1667],
      [1.5,3.5714,4.1667,4.4545,4.4,4.5],
      [2.375,4.375,4.75,4.2857,5,5],
      [1.75,3,4.2727,3.8182,3.8571,4.7143],
      [1.5,4,3.5455,3.8889,3.625,4.75],
      [2,3.9091,4.4,4.8571,4.6364,4.8],
      [2.125,4.6,4.8,5,4.6,5],
      [1.4444,4,4,4.4286,4.6364,5],
      [1.7143,3.7778,4.2308,4.1111,4.875,4.875],
      [2,3.2,4.6154,4.625,4.1818,4.4444],
      [1.8889,3.7143,3.8333,4.3,4.7,4.875],
      [2,4.125,4.8,4.5714,4.6,5],
      [2,4.5455,4.6364,4.75,5,4.8333],
    ])

    def load_MOS(matrix,noise): #check change path names

        list_methods=numpy.array(["SIRI","CUTE","RG67","RGALT","RGEdit2","REAL"])

        for i,method in enumerate(list_methods):
            if method==noise:
                location=i

        length=matrix.shape[0]
        dataset={}
        dataset[noise]={}
        dataset[noise]['mos']=[]

        for i in range(length):
            dataset[noise]['mos'].append(matrix[i][location])
        return dataset


    list_methods=numpy.array(["SIRI","CUTE","RG67","RGALT","RGEdit2"])

    final_mos=[]
    for method in list_methods:
        final=[]
        speakers=["CLB","DBL","RMS","SLT"]
        for speaker in speakers:
            if speaker=='SLT':
                mlsa_mos=load_MOS(mos_SLT,method)
                A2=mlsa_mos[method]['mos']
            elif speaker=='CLB':
                mlsa_mos=load_MOS(mos_CLB,method)
                A2=mlsa_mos[method]['mos']
            elif speaker=='RMS':
                mlsa_mos=load_MOS(mos_RMS,method)
                A2=mlsa_mos[method]['mos']
            elif speaker=='DBL':
                mlsa_mos=load_MOS(mos_DBL,method)
                A2=mlsa_mos[method]['mos']
            final.extend(A2)
        final_mos.extend(final)

    output=np.asarray(final_mos)
    final_mos=[]
    for i in range(20):
        final_mos.append(np.mean(output[i*44:i*44+44]))


    from scipy.stats import pearsonr
    corr, _ = pearsonr(final_mos,final_pesq)
    from scipy.stats import spearmanr
    corr1,_=spearmanr(final_mos,final_pesq)
    print(corr)
    print(corr1)
    
    return [corr,corr1]