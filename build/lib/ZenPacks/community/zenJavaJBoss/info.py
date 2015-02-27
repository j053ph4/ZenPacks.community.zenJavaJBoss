from ZenPacks.community.ConstructionKit.ClassHelper import *

def JBossInfinispanCacheManagergetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class JBossInfinispanCacheManagerInfo(ClassHelper.JBossInfinispanCacheManagerInfo):
    ''''''

def JBossInfinispanClustergetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class JBossInfinispanClusterInfo(ClassHelper.JBossInfinispanClusterInfo):
    ''''''

def JBossInfinispanCachegetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class JBossInfinispanCacheInfo(ClassHelper.JBossInfinispanCacheInfo):
    ''''''

def JBossJGroupClustergetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class JBossJGroupClusterInfo(ClassHelper.JBossJGroupClusterInfo):
    ''''''


