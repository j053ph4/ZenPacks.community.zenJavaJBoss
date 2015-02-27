from ZenPacks.community.ConstructionKit.BasicDefinition import *
from ZenPacks.community.ConstructionKit.Construct import *
from ZenPacks.community.zenJavaApp.Definition import getMBeanDef, addMBeanRelations


ROOT = "ZenPacks.community"
BASE = "zenJavaJBoss"
VERSION = Version(1, 0, 0)


###################### JBossInfinispanCache
ADATA = getMBeanDef(VERSION, ROOT, BASE, 'JBossInfinispanCache','JBoss Infinispan Cache', 'JBoss Infinispan Caches')
ADATA['componentData']['properties']['manager'] = addProperty('Manager', optional=False)


JBossInfinispanCacheDefinition = type('JBossInfinispanCacheDefinition', (BasicDefinition,),ADATA)
addMBeanRelations(JBossInfinispanCacheDefinition)

###################### JBossInfinispanCacheManager
BDATA = getMBeanDef(VERSION, ROOT, BASE, 'JBossInfinispanCacheManager','JBoss Infinispan Cache Mgr', 'JBoss Infinispan Cache Mgrs')
JBossInfinispanCacheManagerDefinition = type('JBossInfinispanCacheManagerDefinition', (BasicDefinition,), BDATA)
addMBeanRelations(JBossInfinispanCacheManagerDefinition)


###################### JBossInfinispanChannel
CDATA = getMBeanDef(VERSION, ROOT, BASE, 'JBossInfinispanCluster','JBoss Infinispan Cluster', 'JBoss Infinispan Clusters')
CDATA['componentData']['properties']['cluster'] = addProperty('Cluster', optional=False)

JBossInfinispanClusterDefinition = type('JBossInfinispanClusterDefinition', (BasicDefinition,), CDATA)
addMBeanRelations(JBossInfinispanClusterDefinition)



###################### JBossJGroupCluster
DDATA = getMBeanDef(VERSION, ROOT, BASE, 'JBossJGroupCluster','JBoss JGroup', 'JBoss JGroups')
DDATA['componentData']['properties']['cluster'] = addProperty('Cluster', optional=False)

JBossJGroupClusterDefinition = type('JBossJGroupClusterDefinition', (BasicDefinition,), DDATA)
addMBeanRelations(JBossJGroupClusterDefinition)


