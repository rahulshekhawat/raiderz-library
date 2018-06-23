#!/usr/bin/env python3
# pylint: disable=C0111
# pylint: disable=C0103
# pylint: disable=W0703

"""
This module contains all the flags used in RaiderZ code that are relevant
to our library
"""


EXPORTER_MESH_VER1 =	0x00000011
EXPORTER_MESH_VER2 =	0x00005001
EXPORTER_MESH_VER3 =	0x00005002
EXPORTER_MESH_VER4 =	0x00005003
EXPORTER_MESH_VER5 =	0x00005004
EXPORTER_MESH_VER6 =	0x00005005
EXPORTER_MESH_VER7 =	0x00005006
EXPORTER_MESH_VER8 =	0x00005007
EXPORTER_MESH_VER9 =	0x00005008
EXPORTER_MESH_VER10 =	0x00005009
EXPORTER_MESH_VER11 =	0x0000500a		
EXPORTER_MESH_VER12 =	0x0000500b		
EXPORTER_MESH_VER13 = 0x0000500c		
EXPORTER_MESH_VER14 = 0x0000500d		
EXPORTER_MESH_VER15 = 0x0000500e		
EXPORTER_MESH_VER16 = 0x0000500f		
EXPORTER_MESH_VER17 = 0x00005010		
EXPORTER_MESH_VER18 = 0x00005011		
EXPORTER_MESH_VER19 = 0x00005012
EXPORTER_MESH_VER20 = 0x00005013

EXPORTER_CURRENT_MESH_VER = EXPORTER_MESH_VER20

EXPORTER_ANI_VER1 =	0x00000012
EXPORTER_ANI_VER2 =	0x00001001
EXPORTER_ANI_VER3 =	0x00001002
EXPORTER_ANI_VER4 =	0x00001003	
EXPORTER_ANI_VER5 =	0x00001004	
EXPORTER_ANI_VER6 =	0x00001005	
EXPORTER_ANI_VER7 =	0x00001006	
EXPORTER_ANI_VER8 =	0x00001007	
EXPORTER_ANI_VER9 =	0x00001008	
EXPORTER_ANI_VER10 =	0x00001009
EXPORTER_ANI_VER11 =	0x00001010
EXPORTER_ANI_VER12 =	0x00001011

EXPORTER_CURRENT_ANI_VER = EXPORTER_ANI_VER12

EXPORTER_SIG	 =	0x0107f060

PHYSIQUE_MAX_WEIGHT	= 3

RM_FLAG_ADDITIVE			 =	0x0001
RM_FLAG_USEOPACITY			 =	0x0002
RM_FLAG_TWOSIDED			 =	0x0004
RM_FLAG_NOTWALKABLE			 =	0x0008		
RM_FLAG_CASTSHADOW			 =	0x0010
RM_FLAG_RECEIVESHADOW		 =	0x0020
RM_FLAG_PASSTHROUGH			 =	0x0040		
RM_FLAG_HIDE				 =	0x0080		
RM_FLAG_PASSBULLET			 =	0x0100		
RM_FLAG_PASSROCKET			 =	0x0200	
RM_FLAG_USEALPHATEST		 =	0x0400		
RM_FLAG_NOSHADE				 =	0x0800
RM_FLAG_AI_NAVIGATION		 =	0x1000		
RM_FLAG_USEPARTSCOLOR		 =	0x80000		
RM_FLAG_TEXTURE_TRANSFORM	 =	0x100000	
RM_FLAG_EXTRA_UV			 =	0x200000	

RM_FLAG_COLLISION_MESH		 =	0x2000
RM_FLAG_DUMMY_MESH			 =	0x4000
RM_FLAG_BONE_MESH			 =	0x10000		# bone mesh
RM_FLAG_LOD_MESH			 =	0xFFFFF		# Temp

RM_FLAG_CLOTH_MESH			 =	0x8000	
RM_FLAG_COLLISION_CLOTH_MESH =	0x20000	
RM_FLAG_COLLISION_MESHONLY	 =	0x40000		# Collision Only (Box, Sphere, and Capsule)

RM_FLAG_OCCLUDER			 =	0x1000000	
