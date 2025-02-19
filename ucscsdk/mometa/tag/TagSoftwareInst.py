"""This module contains the general information for TagSoftwareInst ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class TagSoftwareInstConsts():
    SRC_DME_CENTRAL_MGR = "central-mgr"
    SRC_DME_IDENTIFIER_MGR = "identifier-mgr"
    SRC_DME_MGMT_CONTROLLER = "mgmt-controller"
    SRC_DME_OPERATION_MGR = "operation-mgr"
    SRC_DME_POLICY_MGR = "policy-mgr"
    SRC_DME_RESOURCE_MGR = "resource-mgr"
    SRC_DME_SERVER_MGR = "server-mgr"
    SRC_DME_SERVICE_REG = "service-reg"
    SRC_DME_STATS_MGR = "stats-mgr"
    SRC_DME_UNKNOWN = "unknown"


class TagSoftwareInst(ManagedObject):
    """This is TagSoftwareInst class."""

    consts = TagSoftwareInstConsts()
    naming_props = set([u'defName', u'value', u'taggedObjectDn'])

    mo_meta = MoMeta("TagSoftwareInst", "tagSoftwareInst", "type-[def_name]-inst-[value]-obj-[tagged_object_dn]", VersionMeta.Version151a, "InputOutput", 0x1ff, [], ["aaa", "admin", "ext-lan-config", "ext-lan-policy", "ext-lan-qos", "ext-lan-security", "ext-san-config", "ext-san-policy", "ext-san-qos", "ext-san-security", "fault", "ls-compute", "ls-config", "ls-config-policy", "ls-ext-access", "ls-network", "ls-network-policy", "ls-qos", "ls-qos-policy", "ls-security", "ls-security-policy", "ls-server", "ls-server-oper", "ls-server-policy", "ls-storage", "ls-storage-policy", "operations", "org-management", "pn-equipment", "pn-maintenance", "pn-policy", "pn-security", "pod-config", "pod-policy", "pod-qos", "pod-security", "read-only", "stats-management", "tag"], [u'tagInstanceEp'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "def_dn": MoPropertyMeta("def_dn", "defDn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "def_name": MoPropertyMeta("def_name", "defName", "string", VersionMeta.Version151a, MoPropertyMeta.NAMING, 0x2, None, None, r"""[ !#$%&\(\)\*\+,\-\.:;=\?@\[\]_\{\|\}~a-zA-Z0-9]{1,32}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "object_name": MoPropertyMeta("object_name", "objectName", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\.:;=\?@\[\]_\{\|\}~a-zA-Z0-9]{0,32}""", [], []), 
        "object_type": MoPropertyMeta("object_type", "objectType", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "src_dme": MoPropertyMeta("src_dme", "srcDme", "string", VersionMeta.Version151a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["central-mgr", "identifier-mgr", "mgmt-controller", "operation-mgr", "policy-mgr", "resource-mgr", "server-mgr", "service-reg", "stats-mgr", "unknown"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "tagged_object_dn": MoPropertyMeta("tagged_object_dn", "taggedObjectDn", "string", VersionMeta.Version151a, MoPropertyMeta.NAMING, 0x20, 0, 256, None, [], []), 
        "value": MoPropertyMeta("value", "value", "string", VersionMeta.Version151a, MoPropertyMeta.NAMING, 0x40, 1, 64, None, [], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x80, 0, 510, None, [], []), 
        "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version151a, MoPropertyMeta.READ_WRITE, 0x100, 0, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "defDn": "def_dn", 
        "defName": "def_name", 
        "dn": "dn", 
        "objectName": "object_name", 
        "objectType": "object_type", 
        "rn": "rn", 
        "srcDme": "src_dme", 
        "status": "status", 
        "taggedObjectDn": "tagged_object_dn", 
        "value": "value", 
        "vendor": "vendor", 
        "version": "version", 
    }

    def __init__(self, parent_mo_or_dn, def_name, value, tagged_object_dn, **kwargs):
        self._dirty_mask = 0
        self.def_name = def_name
        self.value = value
        self.tagged_object_dn = tagged_object_dn
        self.child_action = None
        self.def_dn = None
        self.object_name = None
        self.object_type = None
        self.src_dme = None
        self.status = None
        self.vendor = None
        self.version = None

        ManagedObject.__init__(self, "TagSoftwareInst", parent_mo_or_dn, **kwargs)

