"""This module contains the general information for AdaptorHostEthIfProfile ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class AdaptorHostEthIfProfileConsts():
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"


class AdaptorHostEthIfProfile(ManagedObject):
    """This is AdaptorHostEthIfProfile class."""

    consts = AdaptorHostEthIfProfileConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("AdaptorHostEthIfProfile", "adaptorHostEthIfProfile", "eth-profile-[name]", VersionMeta.Version111a, "InputOutput", 0x7f, [], ["read-only"], [u'orgOrg', u'policySystemEp'], [u'adaptorEthAdvFilterProfile', u'adaptorEthArfsProfile', u'adaptorEthCompQueueProfile', u'adaptorEthFailoverProfile', u'adaptorEthGENEVEProfile', u'adaptorEthInterruptProfile', u'adaptorEthInterruptScalingProfile', u'adaptorEthNVGREProfile', u'adaptorEthOffloadProfile', u'adaptorEthRecvQueueProfile', u'adaptorEthRoCEProfile', u'adaptorEthVxLANProfile', u'adaptorEthWorkQueueProfile', u'adaptorExtIpV6RssHashProfile', u'adaptorIpV4RssHashProfile', u'adaptorIpV6RssHashProfile', u'adaptorRssProfile'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "pooled_resources": MoPropertyMeta("pooled_resources", "pooledResources", "string", VersionMeta.Version201f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "pooledResources": "pooled_resources", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.policy_level = None
        self.policy_owner = None
        self.pooled_resources = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorHostEthIfProfile", parent_mo_or_dn, **kwargs)

