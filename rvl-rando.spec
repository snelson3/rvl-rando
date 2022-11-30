# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


import os, glob, khbr, shutil

for root, dirs, files in os.walk(DISTPATH):
    for f in files:
        os.unlink(os.path.join(root, f))
    for d in dirs:
        shutil.rmtree(os.path.join(root, d))


def build_datas_recursive(paths):
  datas = []
  
  for path in paths:
    for filename in glob.iglob(path, recursive=True):
      dest_dirname = os.path.dirname(filename)
      if dest_dirname == "":
        dest_dirname = "."
      
      data_entry = (filename, dest_dirname)
      datas.append(data_entry)
      print(data_entry)
  
  return datas



a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=['bdscript\\bdscript\\obj\\B_EX110\\b_ex.bdscript',
 'bdscript\\bdscript\\obj\\B_EX110_LV99\\b_ex.bdscript',
 'bdscript\\bdscript\\obj\\B_EX110_SKIRMISH\\b_ex.bdscript',
 'bdscript\\bdscript\\obj\\B_EX120_HB_LV99\\b_ex.bdscript',
 'bdscript\\bdscript\\obj\\B_EX130\\b_ex.bdscript',
 'bdscript\\bdscript\\obj\\B_EX130_LV99\\b_ex.bdscript',
 'bdscript\\bdscript\\obj\\B_EX140_LV99\\b_ex.bdscript',
 'bdscript\\bdscript\\obj\\B_EX150\\b_ex.bdscript',
 'bdscript\\bdscript\\obj\\B_EX150_LV99\\b_ex.bdscript',
 'bdscript\\bdscript\\obj\\B_EX160_LV99\\b_ex.bdscript',
 'bdscript\\bdscript\\obj\\B_EX170\\b_ex.bdscript',
 'bdscript\\bdscript\\obj\\B_EX170_LAST\\b_ex.bdscript',
 'bdscript\\bdscript\\obj\\B_EX170_LAST_LV99\\b_ex.bdscript',
 'bdscript\\bdscript\\obj\\B_EX170_LV99\\b_ex.bdscript',
 'bdscript\\bdscript\\obj\\B_EX260\\b_ex.bdscript',
 'bdscript\\bdscript\\obj\\B_EX380\\b_ex.bdscript',
 'bdscript\\bdscript\\obj\\B_EX390\\b_ex.bdscript',
 'bdscript\\bdscript\\obj\\B_EX400\\b_ex.bdscript',
 'bdscript\\bdscript\\obj\\B_EX420\\b_ex.bdscript',
 'bdscript\\bdscript\\obj\\B_HE030\\b_he.bdscript',
 'bdscript\\bdscript\\obj\\B_LK100\\b_lk.bdscript',
 'bdscript\\bdscript\\obj\\B_LK100_00\\b_lk.bdscript',
 'bdscript\\bdscript\\obj\\B_LK100_10\\b_lk.bdscript',
 'bdscript\\bdscript\\obj\\B_LK100_20\\b_lk.bdscript',
 'bdscript\\bdscript\\obj\\B_LK110\\b_lk.bdscript',
 'bdscript\\bdscript\\obj\\F_EH100\\f_eh.bdscript',
 'bdscript\\bdscript\\obj\\M_EX960\\m_ex.bdscript',
 'bdscript\\bdscript\\obj\\N_CM000_BTL\\n_cm.bdscript',
 'bdscript\\bdscript\\obj\\N_CM020_BTL\\n_cm.bdscript',
 'bdscript\\bdscript\\obj\\N_CM040_BTL\\n_cm.bdscript',
 'bdscript\\bdscript\\obj\\N_EX500_BTL\\n_ex.bdscript',
 'bdscript\\bdscript\\obj\\N_EX570_BTL\\n_ex.bdscript',
 'bdscript\\bdscript\\obj\\N_EX600_BTL\\n_ex.bdscript',
 'bdscript\\bdscript\\obj\\N_EX610_BTL\\n_ex.bdscript',
 'bdscript\\bdscript\\obj\\N_EX610_BTL2\\n_ex.bdscript',
 'bdscript\\bdscript\\obj\\N_EX760_BTL\\n_ex.bdscript',
 'bdscript\\bdscript\\obj\\N_HB530_BTL2\\n_hb.bdscript',
 'bdscript\\bdscript\\obj\\N_HB550_BTL2\\n_hb.bdscript',
 'bdscript\\bdscript\\obj\\N_HB570_BTL2\\n_hb.bdscript',
 'bdscript\\bdscript\\obj\\N_HB580_BTL2\\n_hb.bdscript',
 'bdscript\\bdscript\\obj\\N_HE010_BTL_CLSM\\n_he.bdscript',
 'bdscript\\bdscript\\obj\\P_EX100_HTLF_BTL\\p_ex.bdscript',
 'bdscript\\bdscript\\obj\\P_EX130\\p_ex.bdscript'],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)



exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Revenge Value Limit Randomizer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='rando.ico'
)

presetPath = '{0}/presets'.format(DISTPATH)
if os.path.exists(presetPath):
  shutil.rmtree(presetPath)

shutil.copytree('presets', presetPath)

dataPath = '{0}/bdscript'.format(DISTPATH)
if os.path.exists(dataPath):
  shutil.rmtree(dataPath)

shutil.copytree('bdscript', dataPath)
shutil.make_archive('Revenge Limit Value Randomizer', 'zip', DISTPATH)