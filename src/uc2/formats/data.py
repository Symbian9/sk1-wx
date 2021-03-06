# -*- coding: utf-8 -*-
#
# 	Copyright (C) 2012-2016 by Igor E. Novikov
#
# 	This program is free software: you can redistribute it and/or modify
# 	it under the terms of the GNU General Public License as published by
# 	the Free Software Foundation, either version 3 of the License, or
# 	(at your option) any later version.
#
# 	This program is distributed in the hope that it will be useful,
# 	but WITHOUT ANY WARRANTY; without even the implied warranty of
# 	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# 	GNU General Public License for more details.
#
# 	You should have received a copy of the GNU General Public License
# 	along with this program.  If not, see <http://www.gnu.org/licenses/>.

from uc2.uc2const import PDXF, SK1, SK2, SK, SVG, SVGZ, ODG, ORA, \
XCF, SLA, FIG, CDR, CDT, CDRZ, CDTZ, CMX, CCX, CDRX, XAR, AI_PS, AI_PDF, PS, \
EPS, PDF, PSD, CGM, WMF, EMF, XPS, VSD, PLT, HPGL , DXF, DWG, RIFF, XML

from uc2.uc2const import JPG, JP2, TIF, BMP, PCX, GIF, PNG, PPM, XBM, XPM

from uc2.uc2const import SKP, GPL, SCRIBUS_PAL, SOC, CPL, COREL_PAL, ASE, JCW


SIMPLE_LOADERS = []
MODEL_LOADERS = [SK2, SVG, WMF, PLT, SK1, SK, CDR, CDT] + \
[PNG, JPG, JP2, TIF, GIF, BMP, PCX, PPM, XBM, XPM]
PALETTE_LOADERS = [SKP, GPL, SCRIBUS_PAL, SOC, CPL, COREL_PAL, ASE, JCW]
EXPERIMENTAL_LOADERS = [RIFF, CDRZ, XML]

SIMPLE_SAVERS = []
PALETTE_SAVERS = [SKP, GPL, SCRIBUS_PAL, SOC, CPL, COREL_PAL, ASE, JCW]
MODEL_SAVERS = [SK2, SVG, WMF, PLT, PDF, PNG, SK1, SK, ]
EXPERIMENTAL_SAVERS = [RIFF, CDR, XML ]

PATTERN_FORMATS = [EPS, PNG, JPG, JP2, TIF, GIF, BMP, PCX, PPM, XBM, XPM]

LOADER_FORMATS = SIMPLE_LOADERS + MODEL_LOADERS + PALETTE_LOADERS

SAVER_FORMATS = SIMPLE_SAVERS + MODEL_SAVERS + PALETTE_SAVERS

from uc2.formats.sk2 import sk2_loader, sk2_saver, check_sk2
from uc2.formats.pdxf import pdxf_loader, pdxf_saver, check_pdxf
from uc2.formats.pdf import check_pdf, pdf_saver
from uc2.formats.plt import plt_loader, plt_saver, check_plt
from uc2.formats.sk1 import sk1_loader, sk1_saver, check_sk1
from uc2.formats.sk import sk_loader, sk_saver, check_sk
from uc2.formats.svg import svg_loader, svg_saver, check_svg

from uc2.formats.wmf import wmf_loader, wmf_saver, check_wmf

from uc2.formats.cdr import cdr_loader, cdr_saver, check_cdr
from uc2.formats.cdrz import cdrz_loader, check_cdrz
from uc2.formats.riff import riff_loader, riff_saver, check_riff

from uc2.formats.png import png_loader, check_png, png_saver
from uc2.formats.fallback import im_loader, fallback_check

from uc2.formats.skp import skp_loader, skp_saver, check_skp
from uc2.formats.gpl import gpl_loader, gpl_saver, check_gpl
from uc2.formats.scribus_pal import scribus_pal_loader, scribus_pal_saver, \
check_scribus_pal
from uc2.formats.soc import soc_loader, soc_saver, check_soc
from uc2.formats.cpl import cpl_loader, cpl_saver, check_cpl
from uc2.formats.corel_pal import corel_pal_loader, corel_pal_saver, \
check_corel_pal
from uc2.formats.ase import ase_loader, ase_saver, check_ase
from uc2.formats.jcw import jcw_loader, jcw_saver, check_jcw
from uc2.formats.xml_ import xml_loader, xml_saver, check_xml


LOADERS = {
SK2 : sk2_loader, PDXF : pdxf_loader, SK1 : sk1_loader, SK : sk_loader,
SVG : svg_loader, SVGZ : None, ORA : None, XCF : None, SLA : None, FIG : None,
CDR : cdr_loader, CDT : cdr_loader, CDRZ : cdrz_loader, CDTZ : cdrz_loader,
CMX : None, CCX : None, CDRX : None,
XAR : None,
AI_PS : None, AI_PDF : None, PS : None, EPS : None, PDF : None, PSD : None,
CGM : None, WMF : wmf_loader, EMF : None, XPS : None, VSD : None,
PLT : plt_loader, HPGL : None, DXF : None, DWG : None,
RIFF: riff_loader,

PNG: png_loader, JPG: im_loader, JP2: im_loader, TIF: im_loader, GIF: im_loader,
BMP: im_loader, PCX: im_loader, PPM: im_loader, XBM: im_loader, XPM: im_loader,

SKP: skp_loader, GPL:gpl_loader, SCRIBUS_PAL:scribus_pal_loader, SOC:soc_loader,
CPL: cpl_loader, COREL_PAL: corel_pal_loader, ASE: ase_loader, JCW:jcw_loader,

XML: xml_loader,
}

SAVERS = {
SK2 : sk2_saver, PDXF : pdxf_saver, SK1 : sk1_saver, SK : sk_saver,
SVG : svg_saver, SVGZ : None, ORA : None, XCF : None, SLA : None, FIG : None,
CDR : cdr_saver, CDT : None, CDRZ : None, CDTZ : None, CMX : None, CCX : None,
CDRX : None,
XAR : None,
AI_PS : None, AI_PDF : None, PS : None, EPS : None, PDF : pdf_saver, PSD : None,
CGM : None, WMF : wmf_saver, EMF : None, XPS : None, VSD : None,
PLT : plt_saver, HPGL : None, DXF : None, DWG : None,
RIFF: riff_saver,

PNG: png_saver,

SKP: skp_saver, GPL:gpl_saver, SCRIBUS_PAL:scribus_pal_saver, SOC:soc_saver,
CPL: cpl_saver, COREL_PAL: corel_pal_saver, ASE: ase_saver, JCW: jcw_saver,

XML: xml_saver,
}

CHECKERS = {
SK2 : check_sk2, PDXF : check_pdxf, SK1 : check_sk1, SK : check_sk,
SVG : check_svg, SVGZ : None, ORA : None, XCF : None, SLA : None, FIG : None,
CDR : check_cdr, CDT : check_cdr, CDRZ : check_cdrz, CDTZ : check_cdrz,
CMX : None, CCX : None, CDRX : None,
XAR : None,
AI_PS : None, AI_PDF : None, PS : None, EPS : None, PDF : None, PSD : None,
CGM : None, WMF : check_wmf, EMF : None, XPS : None, VSD : None,
PLT : check_plt, HPGL : None, DXF : None, DWG : None,
RIFF: check_riff,
PNG: check_png, JPG: fallback_check, JP2: fallback_check, TIF: fallback_check,
GIF: fallback_check, BMP: fallback_check, PCX: fallback_check,
PPM: fallback_check, XBM: fallback_check, XPM: fallback_check,

SKP: check_skp, GPL: check_gpl, SCRIBUS_PAL:check_scribus_pal, SOC:check_soc,
CPL: check_cpl, COREL_PAL: check_corel_pal, ASE: check_ase, JCW: check_jcw,

XML: check_xml,
}

