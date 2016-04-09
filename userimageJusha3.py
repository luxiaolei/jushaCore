
# coding: utf-8

# In[9]:

import jushacore as mapper 
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import scipy
import json
import sys
#get_ipython().magic(u'matplotlib inline')


# In[10]:

data = 'data/input_data_minmax.csv'
df = pd.read_csv(data)
data = df.ix[:, :-2].values
cont = df.shape[0]
df.shape


# In[11]:

df.head()


# In[12]:

data.shape


# In[13]:

filt = df.ix[:, [-1,-2]].values
filt.shape


# In[14]:

def to_d3js_graph(mapper_output, fn):
    """
    Convert the 1-skeleton of a L{mapper_output} to a dictionary
    designed for exporting to a json package for use with the d3.js
    force-layout graph visualisation system.
    """
    G = {}
    G['vertices'] = [{'index': i, 'level': n.level, 'members':
                      list(n.points), 'attribute': n.attribute}
                     for (i,n) in enumerate(mapper_output.nodes)]
    G['edges'] = [{'source': e[0], 'target': e[1], 'wt':
                   mapper_output.simplices[1][e]} for e in
                  mapper_output.simplices[1].keys()]
    """
    distinctAttr = [i['attribute'] for i in G['vertices']]
    distinctAttr = list(set(distinctAttr))
    distinctAttr.sort()
    G['distinctAttr'] = distinctAttr
    G['colormap'] = genJetColormap(len(distinctAttr))

    #generate two maps for index key-value pairs
    G['indexNameMap']= {}
    G['nameIndexMap']= {}

    for k,v in enumerate(selfvars.df.index):
        G['indexNameMap'][k] = v
        G['nameIndexMap'][v] = k
    """
    
    with open(fn+'.json', 'w') as f:
        json.dump(G, f)
    #save js


# In[15]:

def wrapper(data, interval, overlap, fn):
    cluster = mapper.single_linkage()
    cover = mapper.cover.cube_cover_primitive(interval, overlap)
    metricpar = {'metric': 'euclidean'}
    
    mapper_output = mapper.jushacore(data, filt, cover=cover,                             cutoff=None, cluster=cluster,                             metricpar=metricpar, point_labels=df.index.values)
    mapper.scale_graph(mapper_output, filt, cover=cover, weighting='inverse',                  exponent= 0.)
    
    to_d3js_graph(mapper_output, fn)


# In[ ]:

"""
fns = ['10interval', '20interval', '30interval', '40interval']
fns = ['result/'+i for i in fns]
interval = [10, 20, 30, 40]
for i, f in zip(interval, fns):
"""
i = sys.argv[1]
i = int(i)
print 'interval is:'
print i 

o = float(sys.argv[2])
print 'overlap is'
print o

#name = sys.argv[3]
#name = str(name)
print 'file name is:'
#print name

#p = raw.input('press enter to start!')

name = 'i'+str(i)+'o'+str(int(o))

wrapper(data, i , o, name)#'20interval2')


# In[ ]:



