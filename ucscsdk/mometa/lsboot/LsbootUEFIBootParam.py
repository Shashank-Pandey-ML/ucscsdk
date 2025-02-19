"""This module contains the general information for LsbootUEFIBootParam ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class LsbootUEFIBootParamConsts():
    pass


class LsbootUEFIBootParam(ManagedObject):
    """This is LsbootUEFIBootParam class."""

    consts = LsbootUEFIBootParamConsts()
    naming_props = set([])

    mo_meta = MoMeta("LsbootUEFIBootParam", "lsbootUEFIBootParam", "uefi-boot-param", VersionMeta.Version141a, "InputOutput", 0x7f, [], ["admin", "ls-config-policy", "ls-server-policy", "ls-storage-policy"], [u'lsbootDefaultLocalImage', u'lsbootEmbeddedLocalDiskImage', u'lsbootEmbeddedLocalDiskImagePath', u'lsbootEmbeddedLocalLunImage', u'lsbootIScsiImagePath', u'lsbootLanImagePath', u'lsbootLocalDiskImage', u'lsbootLocalDiskImagePath', u'lsbootLocalHddImage', u'lsbootLocalLunImagePath', u'lsbootNvme', u'lsbootSanCatSanImagePath', u'lsbootSanImagePath', u'lsbootUsbExternalImage', u'lsbootUsbFlashStorageImage', u'lsbootUsbInternalImage'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "boot_description": MoPropertyMeta("boot_description", "bootDescription", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, [], []), 
        "boot_loader_name": MoPropertyMeta("boot_loader_name", "bootLoaderName", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, [], []), 
        "boot_loader_path": MoPropertyMeta("boot_loader_path", "bootLoaderPath", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "bootDescription": "boot_description", 
        "bootLoaderName": "boot_loader_name", 
        "bootLoaderPath": "boot_loader_path", 
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.boot_description = None
        self.boot_loader_name = None
        self.boot_loader_path = None
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "LsbootUEFIBootParam", parent_mo_or_dn, **kwargs)

