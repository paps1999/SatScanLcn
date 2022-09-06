# for localized messages
from . import _
from enigma import eDVBFrontendParametersSatellite

M7_0192_transponder = {
	"frequency": 12515000,
	"symbol_rate": 22000000,
	"polarization": eDVBFrontendParametersSatellite.Polarisation_Horizontal,
	"fec_inner": eDVBFrontendParametersSatellite.FEC_5_6,
	"orbital_position": 192,
	"system": eDVBFrontendParametersSatellite.System_DVB_S,
	"modulation": eDVBFrontendParametersSatellite.Modulation_QPSK,
	"roll_off": eDVBFrontendParametersSatellite.RollOff_alpha_0_35,
	"original_network_id": 0x0035,
	"transport_stream_id": 0x0451,
}

M7_3592_transponder = {
	"frequency": 11727000,
	"symbol_rate": 28000000,
	"polarization": eDVBFrontendParametersSatellite.Polarisation_Vertical,
	"fec_inner": eDVBFrontendParametersSatellite.FEC_Auto,
	"orbital_position": 3592,
	"system": eDVBFrontendParametersSatellite.System_DVB_S,
	"modulation": eDVBFrontendParametersSatellite.Modulation_QPSK,
	"roll_off": eDVBFrontendParametersSatellite.FEC_Auto,
	"original_network_id": 1536,
	"transport_stream_id": 701,
}

PROVIDERS = {
	"Austriasat": {
		"name": _("Austriasat"),
		"transponder": M7_0192_transponder,
		"nit": {
			"nit_pid": 0x3b6,
			"nit_current_table_id": 0xbc,
			"nit_other_table_id": 0x00,
		},
	},
	"BIS_TV_3550": {
		"name": _("BIS TV (5.0W)"),
		"transponder": {
			"frequency": 11512000,
			"symbol_rate": 29950000,
			"polarization": eDVBFrontendParametersSatellite.Polarisation_Vertical,
			"fec_inner": eDVBFrontendParametersSatellite.FEC_2_3,
			"orbital_position": 3550,
			"system": eDVBFrontendParametersSatellite.System_DVB_S2,
			"modulation": eDVBFrontendParametersSatellite.Modulation_8PSK,
			"roll_off": eDVBFrontendParametersSatellite.RollOff_auto,
			"original_network_id": 1375,
			"transport_stream_id": 20200,
		},
		"bat": {
			"BouquetID": 0x0551,
		},
		"sdt": {
			"sdt_only_scan_home": True,
		},
	},
	"BIS_TV_0130": {
		"name": _("BIS TV (13.0E)"),
		"transponder": {
			"frequency": 11681000,
			"symbol_rate": 27500000,
			"polarization": eDVBFrontendParametersSatellite.Polarisation_Horizontal,
			"fec_inner": eDVBFrontendParametersSatellite.FEC_3_4,
			"orbital_position": 130,
			"system": eDVBFrontendParametersSatellite.System_DVB_S2,
			"modulation": eDVBFrontendParametersSatellite.Modulation_8PSK,
			"roll_off": eDVBFrontendParametersSatellite.RollOff_auto,
			"original_network_id": 319,
			"transport_stream_id": 15900,
		},
		"bat": {
			"BouquetID": 0x0132,
		},
		"sdt": {
			"sdt_only_scan_home": True,
		},
	},
	"Canal_Digitaal_HD": {
		"name": _("Canal Digitaal HD"),
		"transponder": M7_0192_transponder,
		"nit": {
			"nit_pid": 0x385,
			"nit_current_table_id": 0xbc,
			"nit_other_table_id": 0x00,
		},
	},
	"Canal_Digital_Nordic_3592": {
		"name": _("Canal Digital Nordic"),
		"transponder": {
			"frequency": 12418000,
			"symbol_rate": 28000000,
			"polarization": eDVBFrontendParametersSatellite.Polarisation_Vertical,
			"fec_inner": eDVBFrontendParametersSatellite.FEC_7_8,
			"orbital_position": 3592,
			"system": eDVBFrontendParametersSatellite.System_DVB_S,
			"modulation": eDVBFrontendParametersSatellite.Modulation_QPSK,
			"roll_off": eDVBFrontendParametersSatellite.RollOff_auto,
			"original_network_id": 70,
			"transport_stream_id": 20,
		},
		"nit": {
			"nit_lcn_descriptor": 0x87,
			"nit_other_table_id": 0x00,
			"BouquetID": 0x1,
			"BouquetIDs": {
				"Denmark": 0x1,
				"Finland": 0x2,
				"Norway": 0x3,
				"Sweden": 0x4,
			}
		},
		"sdt": {
			"sdt_only_scan_home": True,
		},
	},
	"D_Smart_0420": {
		"name": _("D-Smart"),
		"transponder": {
			"frequency": 12034000,
			"symbol_rate": 27500000,
			"polarization": eDVBFrontendParametersSatellite.Polarisation_Vertical,
			"fec_inner": eDVBFrontendParametersSatellite.FEC_5_6,
			"orbital_position": 420,
			"system": eDVBFrontendParametersSatellite.System_DVB_S,
			"modulation": eDVBFrontendParametersSatellite.Modulation_QPSK,
			"roll_off": eDVBFrontendParametersSatellite.RollOff_auto,
			"original_network_id": 66,
			"transport_stream_id": 3,
		},
		"bat": {
			"bat_lcn_descriptor": 0xe2,
			"BouquetID": 0x6050,
			"bat_regions": { # ( BouquetID,) # Some of these need removing.
				'DOGAN TV - TICARI HDS': (0x6050,),
				'DOGAN TV - TKC': (0x6051,),
				'DOGAN TV - PDL TEST': (0x6052,),
				'DOGAN TV - TKC_TV': (0x6053,),
				'DOGAN TV - HD': (0x6058,),
				'DOGAN TV - HOTBIRD - HD': (0x6059,),
				'DOGAN TV - HOTBIRD - HD - FTA': (0x605a,),
				'DOGAN TV': (0x6090,),
				'DOGAN TV - HOTBIRD': (0x6091,),
				'DOGAN TV - TICARI': (0x6095,),
				'DOGAN TV - HD TESHIR': (0x6096,),
				'DOGAN TV - AVRUPA HOTBIRD': (0x6098,),
				'DOGAN TV - SUSPEND': (0x6099,),
				'DOGAN TV - SUSPEND': (0x609a,),
				'DOGAN TV - MCR': (0x609b,),
				'DOGAN TV - MCR HOTBIRD': (0x609c,),
				'DOGAN TV - MCR - HD': (0x609d,),
				'DOGAN TV - OTELLER': (0x609e,),
				'DOGAN TV - OTELLER PLUS': (0x609f,),
			}
		},
		"sdt": {
			"sdt_only_scan_home": True,
		},
	},
	"Digi_TV_3592": {
		"name": _("Digi TV"),
		"transponder": {
			"frequency": 12687000,
			"symbol_rate": 27500000,
			"polarization": eDVBFrontendParametersSatellite.Polarisation_Horizontal,
			"fec_inner": eDVBFrontendParametersSatellite.FEC_Auto,
			"orbital_position": 3592,
			"system": eDVBFrontendParametersSatellite.System_DVB_S,
			"modulation": eDVBFrontendParametersSatellite.Modulation_QPSK,
			"roll_off": eDVBFrontendParametersSatellite.RollOff_auto,
			"original_network_id": 1,
			"transport_stream_id": 1,
		},
		"bat": {
			"bat_lcn_descriptor": 0x86,
			"BouquetID": 0x110,
			"bat_region": (0x3f,), # area, this is just the default.
			"bat_regions": { # ( BouquetID,)
				'Romania SD': (0x32,),
				'Hungary SD': (0x33,),
				'Slovakia SD': (0x34,),
				'Croatia SD': (0x35,),
				'Czech SD': (0x36,),
				'Serbia SD': (0x37,),
				'All SD': (0x38,),
				'Romania HD': (0x39,),
				'Hungary HD': (0x3a,),
				'Slovakia HD': (0x3b,),
				'Croatia HD': (0x3c,),
				'Czech HD': (0x3d,),
				'Serbia HD': (0x3e,),
				'All HD': (0x3f,),
			}
		},
		"sdt": {
			"sdt_only_scan_home": True,
		},
	},
	"Diveo_0192": {
		"name": _("Diveo"),
		"transponder": M7_0192_transponder,
		"nit": {
			"nit_pid": 0x3c0,
			"nit_current_table_id": 0xbc,
			"nit_other_table_id": 0x00,
		},
	},
	"FocusSAT_3920": {
		"name": _("FocusSat"),
		"transponder": M7_3592_transponder,
		"nit": {
			"nit_pid": 0x54,
			"nit_current_table_id": 0xbc,
			"nit_other_table_id": 0x00,
		},
	},
	"Fransat_3550": {
		"name": _("Fransat"),
		"transponder": {
			"frequency": 10972000,
			"symbol_rate": 29950000,
			"polarization": eDVBFrontendParametersSatellite.Polarisation_Vertical,
			"fec_inner": eDVBFrontendParametersSatellite.FEC_2_3,
			"orbital_position": 3550,
			"system": eDVBFrontendParametersSatellite.System_DVB_S2,
			"modulation": eDVBFrontendParametersSatellite.Modulation_8PSK,
			"roll_off": eDVBFrontendParametersSatellite.RollOff_auto,
			"original_network_id": 1375,
			"transport_stream_id": 20600,
		},
		"bat": {
			"BouquetID": 0x71,
		},
		"sdt": {
			"sdt_only_scan_home": True,
		},
	},
	"French_TNT_0130": {
		"name": _("French_TNT"),
		"transponder": {
			"frequency": 11856000,
			"symbol_rate": 29700000,
			"polarization": eDVBFrontendParametersSatellite.Polarisation_Vertical,
			"fec_inner": eDVBFrontendParametersSatellite.FEC_2_3,
			"orbital_position": 192,
			"system": eDVBFrontendParametersSatellite.System_DVB_S2,
			"modulation": eDVBFrontendParametersSatellite.Modulation_8PSK,
			"roll_off": eDVBFrontendParametersSatellite.RollOff_auto,
			"original_network_id": 1,
			"transport_stream_id": 1072,
		},
		"nit": {
			"nit_other_table_id": 0x00,
		},
		"bat": {
			"BouquetID": 0xc00f,
			"bat_regions": { # ( BouquetID,)
				'CanalSat': (0xc001,),
				'TNT SAT': (0xc00f,),
			}
		},
		"sdt": {
			"sdt_only_scan_home": True,
		},
	},
	"FreeSAT_CZ_3920": {
		"name": _("FreeSAT CZ"),
		"transponder": M7_3592_transponder,
		"nit": {
			"nit_pid": 0x53,
			"nit_current_table_id": 0xbc,
			"nit_other_table_id": 0x00,
		},
	},
	"FreeSAT_SK_3920": {
		"name": _("FreeSAT SK"),
		"transponder": M7_3592_transponder,
		"nit": {
			"nit_pid": 0x53,
			"nit_current_table_id": 0xbc,
			"nit_other_table_id": 0x00,
		},
	},
	"Freesat_UK_0282": {
		"name": _("Freesat UK"),
		"transponder": {
			"frequency": 11426000,
			"symbol_rate": 27500000,
			"polarization": eDVBFrontendParametersSatellite.Polarisation_Horizontal,
			"fec_inner": eDVBFrontendParametersSatellite.FEC_Auto,
			"orbital_position": 282,
			"system": eDVBFrontendParametersSatellite.System_DVB_S,
			"modulation": eDVBFrontendParametersSatellite.Modulation_QPSK,
			"roll_off": eDVBFrontendParametersSatellite.RollOff_auto,
			"original_network_id": 59,
			"transport_stream_id": 2315,
		},
		"nit": {
			"nit_other_table_id": 0x00,
		},
		"bat": {
			"bat_lcn_descriptor": 0xd3,
			"BouquetID": 0x110,
			"bat_region": (0x1, 0xffff), # area and common channels, this is just the default.
			"bat_pid": 0xbba,
			"bat_regions": { # ( BouquetID, (region, common_catchall))
				'BBC London/ITV London': (0x110, (0x1, 0xffff)),
				'BBC East (W)/ITV Anglia W': (0x110, (0x2, 0xffff)),
				'BBC East (W)/ITV Central S': (0x110, (0x3, 0xffff)),
				'BBC East (W)/ITV Anglia W': (0x110, (0x4, 0xffff)),
				'BBC W Mids/ITV Central W': (0x110, (0x5, 0xffff)),
				'BBC W Mids/ITV Central SW': (0x110, (0x6, 0xffff)),
				'BBC N West/ITV Granada': (0x110, (0x7, 0xffff)),
				'BBC N West/ITV BorderEng': (0x110, (0x8, 0xffff)),
				'BBC EYrks&amp;Lin/ITV Yorkshire E': (0x110, (0x9, 0xffff)),
				'BBC Yorkshire/ITV Yorkshire W': (0x110, (0xa, 0xffff)),
				'BBC Yorkshire/ITV Yorkshire E': (0x110, (0xb, 0xffff)),
				'BBC Yorkshire/ITV Tyne Tees S': (0x110, (0xc, 0xffff)),
				'BBC E Midlands/ITV Central E': (0x110, (0xd, 0xffff)),
				'BBC E Midlands/ITV Central W': (0x110, (0xe, 0xffff)),
				'BBC E Midlands/ITV Central E': (0x110, (0xf, 0xffff)),
				'BBC E Midlands/ITV Yorkshire E': (0x110, (0x10, 0xffff)),
				'BBC East (E)/ITV Anglia S': (0x110, (0x11, 0xffff)),
				'BBC East (E)/ITV London': (0x110, (0x12, 0xffff)),
				'BBC East (E)/ITV Anglia E': (0x110, (0x13, 0xffff)),
				'BBC West/Westcountry W': (0x110, (0x14, 0xffff)),
				'BBC West/ITV Westcountry W': (0x110, (0x15, 0xffff)),
				'BBC West/ITV Meridian Thames Valley': (0x110, (0x16, 0xffff)),
				'BBC West/ITV Meridian Thames Valley': (0x110, (0x17, 0xffff)),
				'BBC S East/ITV Meridian S': (0x110, (0x18, 0xffff)),
				'BBC S East/ITV Meridian SE': (0x110, (0x19, 0xffff)),
				'BBC S East/ITV Meridian E': (0x110, (0x1a, 0xffff)),
				'BBC S East/ITV London': (0x110, (0x1b, 0xffff)),
				'BBC South/ITV Meridian S': (0x110, (0x1c, 0xffff)),
				'BBC South/ITV Meridian SE': (0x110, (0x1d, 0xffff)),
				'BBC South/ITV W Country': (0x110, (0x1e, 0xffff)),
				'BBC South/ITV London': (0x110, (0x1f, 0xffff)),
				'BBC South/ITV Meridian N': (0x110, (0x20, 0xffff)),
				'BBC S West/ITV W Country': (0x110, (0x21, 0xffff)),
				'BBC NE &amp; C/ITV BorderEng': (0x110, (0x22, 0xffff)),
				'BBC NE &amp; C/ITV Tyne Tees N': (0x110, (0x23, 0xffff)),
				'BBC NE &amp; C/ITV Tyne Tees S': (0x110, (0x24, 0xffff)),
				'BBC Oxford/ITV Central S': (0x110, (0x25, 0xffff)),
				'BBC Oxford/ITV London': (0x110, (0x26, 0xffff)),
				'BBC N West/ITV Granada': (0x110, (0x27, 0xffff)),
				'BBC Yorkshire/ITV Yorkshire W': (0x110, (0x28, 0xffff)),
				'BBC Channel Is/ITV Channel Is': (0x110, (0x29, 0xffff)),
				'BBC Yorkshire/ITV Yorkshire W': (0x110, (0x2a, 0xffff)),
				'BBC Isle of Man': (0x110, (0x2b, 0xffff)),
				'BBC Scotland/STV North': (0x111, (0x3c, 0xffff)),
				'BBC Scotland/STV Tayside': (0x111, (0x3d, 0xffff)),
				'BBC Scotland/STV BorderSco': (0x111, (0x3e, 0xffff)),
				'BBC Scotland/STV Scot (Glasgow)': (0x111, (0x3f, 0xffff)),
				'BBC Scotland/STV Scot (Edinburgh)': (0x111, (0x40, 0xffff)),
				'BBC Wales': (0x112, (0x50, 0xffff)),
				'BBC Northern Ireland': (0x113, (0x5a, 0xffff)),
			}
		},
		"sdt": {
			"sdt_pid": 0xbba,
			"sdt_only_scan_home": True,
		},
	},
	"Movistar_plus_esp_0192": {
		"name": _("Movistar+"),
		"transponder": {
			"frequency": 10729000,
			"symbol_rate": 22000000,
			"polarization": eDVBFrontendParametersSatellite.Polarisation_Vertical,
			"fec_inner": eDVBFrontendParametersSatellite.FEC_2_3,
			"orbital_position": 192,
			"system": eDVBFrontendParametersSatellite.System_DVB_S2,
			"modulation": eDVBFrontendParametersSatellite.Modulation_8PSK,
			"roll_off": eDVBFrontendParametersSatellite.RollOff_auto,
			"original_network_id": 1,
			"transport_stream_id": 1050,
		},
		"nit": {
			"nit_other_table_id": 0x00,
		},
		"bat": {
			"BouquetID": 0x21,
		},
		"sdt": {
			"sdt_only_scan_home": True,
		},
		"flags": {
			"ignore_visible_service_flag": True,
		},
	},
	"NC_plus_0130": {
		"name": _("NC+"),
		"transponder": {
			"frequency": 10719000,
			"symbol_rate": 27500000,
			"polarization": eDVBFrontendParametersSatellite.Polarisation_Vertical,
			"fec_inner": eDVBFrontendParametersSatellite.FEC_3_4,
			"orbital_position": 130,
			"system": eDVBFrontendParametersSatellite.System_DVB_S2,
			"modulation": eDVBFrontendParametersSatellite.Modulation_8PSK,
			"roll_off": eDVBFrontendParametersSatellite.RollOff_auto,
			"original_network_id": 318,
			"transport_stream_id": 11000,
		},
		"bat": {
			"BouquetID": 0x2020,
		},
		"sdt": {
			"sdt_only_scan_home": True,
		},
	},
	"NOS_3300": {
		"name": _("NOS"),
		"transponder": {
			"frequency": 12360000,
			"symbol_rate": 27500000,
			"polarization": eDVBFrontendParametersSatellite.Polarisation_Horizontal,
			"fec_inner": eDVBFrontendParametersSatellite.FEC_3_4,
			"orbital_position": 3300,
			"system": eDVBFrontendParametersSatellite.System_DVB_S2,
			"modulation": eDVBFrontendParametersSatellite.Modulation_8PSK,
			"roll_off": eDVBFrontendParametersSatellite.RollOff_auto,
			"original_network_id": 54,
			"transport_stream_id": 38,
		},
		"nit": {
			"nit_lcn_descriptor": 0x82,
			"nit_other_table_id": 0x00,
		},
		"sdt": {
			"sdt_only_scan_home": True,
		},
	},
	"Nova_0130": {
		"name": _("Nova"),
		"transponder": {
			"frequency": 11823000,
			"symbol_rate": 27500000,
			"polarization": eDVBFrontendParametersSatellite.Polarisation_Horizontal,
			"fec_inner": eDVBFrontendParametersSatellite.FEC_3_4,
			"orbital_position": 130,
			"system": eDVBFrontendParametersSatellite.System_DVB_S2,
			"modulation": eDVBFrontendParametersSatellite.Modulation_8PSK,
			"roll_off": eDVBFrontendParametersSatellite.RollOff_auto,
			"original_network_id": 318,
			"transport_stream_id": 5500,
		},
		"bat": {
			"bat_lcn_descriptor": 0x93,
			"BouquetID": 0x1,
			"bat_regions": { # ( BouquetID,)
				'Greece': (0x1,),
				'Cyprus': (0x3,),
			}
		},
		"sdt": {
			"sdt_only_scan_home": True,
		},
	},
	"Orange_TV_0160": {
		"name": _("Orange TV"),
		"transponder": {
			"frequency": 11324000,
			"symbol_rate": 30000000,
			"polarization": eDVBFrontendParametersSatellite.Polarisation_Vertical,
			"fec_inner": eDVBFrontendParametersSatellite.FEC_2_3,
			"orbital_position": 160,
			"system": eDVBFrontendParametersSatellite.System_DVB_S2,
			"modulation": eDVBFrontendParametersSatellite.Modulation_8PSK,
			"roll_off": eDVBFrontendParametersSatellite.RollOff_alpha_0_20,
			"original_network_id": 0x016e,
			"transport_stream_id": 0x9e98,
		},
	},
	"Sky_Italia_0130": {
		"name": _("Sky Italia"),
		"transponder": {
			"frequency": 11976000,
			"symbol_rate": 29900000,
			"polarization": eDVBFrontendParametersSatellite.Polarisation_Horizontal,
			"fec_inner": eDVBFrontendParametersSatellite.FEC_5_6,
			"orbital_position": 130,
			"system": eDVBFrontendParametersSatellite.System_DVB_S2,
			"modulation": eDVBFrontendParametersSatellite.Modulation_QPSK,
			"roll_off": eDVBFrontendParametersSatellite.RollOff_auto,
			"original_network_id": 64511,
			"transport_stream_id": 6300,
		},
		"nit": {
			"nit_other_table_id": 0x00,
		},
		"bat": {
			"bat_lcn_descriptor": 0xb1,
			"BouquetID": 0x6250,
			"bat_region": [0x0, 0xff], # area and common channels
			"bat_regions": {
				'Sky Italia SD': (0x6250, (0x0, 0xff)),
				'Sky Italia HD': (0x6250, (0x4, 0xff)),
			}
		},
		"sdt": {
			"sdt_only_scan_home": True,
		},
	},
	"Sky_UK_0282": {
		"name": _("Sky UK"),
		"transponder": {
			"frequency": 11778000,
			"symbol_rate": 27500000,
			"polarization": eDVBFrontendParametersSatellite.Polarisation_Vertical,
			"fec_inner": eDVBFrontendParametersSatellite.FEC_Auto,
			"orbital_position": 282,
			"system": eDVBFrontendParametersSatellite.System_DVB_S,
			"modulation": eDVBFrontendParametersSatellite.Modulation_QPSK,
			"roll_off": eDVBFrontendParametersSatellite.RollOff_auto,
			"original_network_id": 2,
			"transport_stream_id": 2004,
		},
		"nit": {
			"nit_other_table_id": 0x00,
		},
		"bat": {
			"bat_lcn_descriptor": 0xb1,
			"BouquetID": 0x1005,
			"bat_region": [0x1, 0xff], # area and common channels
			"bat_regions": {
				'Atherstone HD': (0x1005, (0x13, 0xff)),
				'Border England HD': (0x1005, (0x0c, 0xff)),
				'Border Scotland HD': (0x1006, (0x24, 0xff)),
				'Brighton HD': (0x1007, (0x41, 0xff)),
				'Central Midlands HD': (0x1005, (0x03, 0xff)),
				'Channel Isles HD': (0x1008, (0x22, 0xff)),
				'Dundee HD': (0x1006, (0x27, 0xff)),
				'East Midlands HD': (0x1005, (0x14, 0xff)),
				'Essex HD': (0x1005, (0x02, 0xff)),
				'Gloucester HD': (0x1005, (0x18, 0xff)),
				'Grampian HD': (0x1006, (0x23, 0xff)),
				'Granada HD': (0x1005, (0x07, 0xff)),
				'Henley On Thames HD': (0x1007, (0x46, 0xff)),
				'HTV Wales HD': (0x1007, (0x2b, 0xff)),
				'HTV West HD': (0x1005, (0x04, 0xff)),
				'HTV West / Thames Valley HD': (0x1007, (0x3f, 0xff)),
				'Humber HD': (0x1005, (0x1d, 0xff)),
				'London HD': (0x1005, (0x01, 0xff)),
				'London / Essex HD': (0x1005, (0x12, 0xff)),
				'London / Kent HD': (0x1007, (0x40, 0xff)),
				'London / Thames Valley HD': (0x1007, (0x42, 0xff)),
				'Meridian East HD': (0x1005, (0x0b, 0xff)),
				'Meridian North HD': (0x1007, (0x44, 0xff)),
				'Meridian South HD': (0x1005, (0x05, 0xff)),
				'Meridian South East HD': (0x1005, (0x0a, 0xff)),
				'Merseyside HD': (0x1007, (0x2d, 0xff)),
				'Norfolk HD': (0x1005, (0x15, 0xff)),
				'North East Midlands HD': (0x1007, (0x3e, 0xff)),
				'North West Yorkshire HD': (0x1005, (0x08, 0xff)),
				'North Yorkshire HD': (0x1005, (0x1a, 0xff)),
				'Northern Ireland HD': (0x1008, (0x21, 0xff)),
				'Oxford HD': (0x1007, (0x47, 0xff)),
				'Ridge Hill HD': (0x1007, (0x29, 0xff)),
				'Scarborough HD': (0x1007, (0x3d, 0xff)),
				'Scottish East HD': (0x1006, (0x26, 0xff)),
				'Scottish West HD': (0x1006, (0x25, 0xff)),
				'Sheffield HD': (0x1007, (0x3c, 0xff)),
				'South Lakeland HD': (0x1005, (0x1c, 0xff)),
				'South Yorkshire HD': (0x1007, (0x48, 0xff)),
				'Tees HD': (0x1007, (0x45, 0xff)),
				'Thames Valley HD': (0x1005, (0x09, 0xff)),
				'Tring HD': (0x1005, (0x1b, 0xff)),
				'Tyne HD': (0x1005, (0x0d, 0xff)),
				'Wales HD': (0x1008, (0x20, 0xff)),
				'West Anglia HD': (0x1005, (0x19, 0xff)),
				'West Dorset HD': (0x1007, (0x43, 0xff)),
				'Westcountry HD': (0x1005, (0x06, 0xff)),
				'Atherstone SD': (0x1001, (0x13, 0xff)),
				'Border England SD': (0x1001, (0x0c, 0xff)),
				'Border Scotland SD': (0x1002, (0x24, 0xff)),
				'Brighton SD': (0x1003, (0x41, 0xff)),
				'Central Midlands SD': (0x1001, (0x03, 0xff)),
				'Channel Isles SD': (0x1004, (0x22, 0xff)),
				'Dundee SD': (0x1002, (0x27, 0xff)),
				'East Midlands SD': (0x1001, (0x14, 0xff)),
				'Essex SD': (0x1001, (0x02, 0xff)),
				'Gloucester SD': (0x1001, (0x18, 0xff)),
				'Grampian SD': (0x1002, (0x23, 0xff)),
				'Granada SD': (0x1001, (0x07, 0xff)),
				'Henley On Thames SD': (0x1003, (0x46, 0xff)),
				'HTV Wales SD': (0x1003, (0x2b, 0xff)),
				'HTV West SD': (0x1001, (0x04, 0xff)),
				'HTV West / Thames Valley SD': (0x1003, (0x3f, 0xff)),
				'Humber SD': (0x1001, (0x1d, 0xff)),
				'London SD': (0x1001, (0x01, 0xff)),
				'London / Essex SD': (0x1001, (0x12, 0xff)),
				'London / Kent SD': (0x1003, (0x40, 0xff)),
				'London / Thames Valley SD': (0x1003, (0x42, 0xff)),
				'Meridian East SD': (0x1001, (0x0b, 0xff)),
				'Meridian North SD': (0x1003, (0x44, 0xff)),
				'Meridian South SD': (0x1001, (0x05, 0xff)),
				'Meridian South East SD': (0x1001, (0x0a, 0xff)),
				'Merseyside SD': (0x1003, (0x2d, 0xff)),
				'Norfolk SD': (0x1001, (0x15, 0xff)),
				'North East Midlands SD': (0x1003, (0x3e, 0xff)),
				'North West Yorkshire SD': (0x1001, (0x08, 0xff)),
				'North Yorkshire SD': (0x1001, (0x1a, 0xff)),
				'Northern Ireland SD': (0x1004, (0x21, 0xff)),
				'Oxford SD': (0x1003, (0x47, 0xff)),
				'Ridge Hill SD': (0x1003, (0x29, 0xff)),
				'Scarborough SD': (0x1003, (0x3d, 0xff)),
				'Scottish East SD': (0x1002, (0x26, 0xff)),
				'Scottish West SD': (0x1002, (0x25, 0xff)),
				'Sheffield SD': (0x1003, (0x3c, 0xff)),
				'South Lakeland SD': (0x1001, (0x1c, 0xff)),
				'South Yorkshire SD': (0x1003, (0x48, 0xff)),
				'Tees SD': (0x1003, (0x45, 0xff)),
				'Thames Valley SD': (0x1001, (0x09, 0xff)),
				'Tring SD': (0x1001, (0x1b, 0xff)),
				'Tyne SD': (0x1001, (0x0d, 0xff)),
				'Wales SD': (0x1004, (0x20, 0xff)),
				'West Anglia SD': (0x1001, (0x19, 0xff)),
				'West Dorset SD': (0x1003, (0x43, 0xff)),
				'Westcountry SD': (0x1001, (0x06, 0xff)),
				'ROI HD': (0x1008, (0x32, 0xff)),
				'ROI SD': (0x1004, (0x32, 0xff)),
			}
		},
		"sdt": {
			"sdt_only_scan_home": True,
		},
	},
	"Telekom_Romania_0390": {
		"name": _("Telekom Romania"),
		"transponder": {
			"frequency": 12524000,
			"symbol_rate": 30000000,
			"polarization": eDVBFrontendParametersSatellite.Polarisation_Vertical,
			"fec_inner": eDVBFrontendParametersSatellite.FEC_Auto,
			"orbital_position": 390,
			"system": eDVBFrontendParametersSatellite.System_DVB_S,
			"modulation": eDVBFrontendParametersSatellite.Modulation_QPSK,
			"roll_off": eDVBFrontendParametersSatellite.RollOff_auto,
			"original_network_id": 28,
			"transport_stream_id": 13,
		},
		"bat": {
			"bat_lcn_descriptor": 0xe2,
			"BouquetID": 0x6080,
			"bat_regions": { # ( BouquetID,)
				'Bouquet 1': (0x6080,),
				'Bouquet 2': (0x6081,),
				'Bouquet 3 (NewCardOnly)': (0x6157,),
			}
		},
		"sdt": {
			"sdt_only_scan_home": True,
		},
	},
	"TeleSAT_0192": {
		"name": _("TeleSAT"),
		"transponder": M7_0192_transponder,
		"nit": {
			"nit_pid": 0x399,
			"nit_current_table_id": 0xbc,
			"nit_other_table_id": 0x00,
		},
	},
	"Tivusat_0130": {
		"name": _("Tivusat"),
		"transponder": {
			"frequency": 10992000,
			"symbol_rate": 27500000,
			"polarization": eDVBFrontendParametersSatellite.Polarisation_Vertical,
			"fec_inner": eDVBFrontendParametersSatellite.FEC_2_3,
			"orbital_position": 130,
			"system": eDVBFrontendParametersSatellite.System_DVB_S,
			"modulation": eDVBFrontendParametersSatellite.Modulation_QPSK,
			"roll_off": eDVBFrontendParametersSatellite.RollOff_auto,
			"original_network_id": 318,
			"transport_stream_id": 12400,
		},
		"sdt": {
			"sdt_only_scan_home": True,
		},
	},
	"TV_Vlaanderen_0192": {
		"name": _("TV Vlaanderen"),
		"transponder": M7_0192_transponder,
		"nit": {
			"nit_pid": 0x38f,
			"nit_current_table_id": 0xbc,
			"nit_other_table_id": 0x00,
		},
	},
	"UPC_3592": {
		"name": _("UPC"),
		"transponder": {
			"frequency": 12034000,
			"symbol_rate": 30000000,
			"polarization": eDVBFrontendParametersSatellite.Polarisation_Vertical,
			"fec_inner": eDVBFrontendParametersSatellite.FEC_3_4,
			"orbital_position": 3592,
			"system": eDVBFrontendParametersSatellite.System_DVB_S2,
			"modulation": eDVBFrontendParametersSatellite.Modulation_8PSK,
			"roll_off": eDVBFrontendParametersSatellite.RollOff_auto,
			"original_network_id": 1536,
			"transport_stream_id": 705,
		},
		"bat": {
			"BouquetID": 0x2011,
			"bat_lcn_descriptor": 0x81,
			"bat_regions": {
				'Hungary': (0x2011,),
				'Czech Republic': (0x2012,),
				'Slovakia': (0x2013,),
				'Romania': (0x2014,),
				'Moldavia': (0x220d,),
			}
		},
		"sdt": {
			"sdt_only_scan_home": True,
		},
	},
	"UPC_Direct_3920": {
		"name": _("UPC Direct"),
		"transponder": M7_3592_transponder,
		"nit": {
			"nit_pid": 0x51,
			"nit_current_table_id": 0xbc,
			"nit_other_table_id": 0x00,
		},
	},
}