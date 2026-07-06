# render_check.py
# Verification pipeline: docx -> PDF (Word COM) -> page PNGs (PyMuPDF).
# Usage: python templates/render_check.py <file.docx> <out_dir> [dpi]
# Emits out_dir/page-NN.png for visual inspection.

import os
import subprocess
import sys


def docx_to_pdf(docx_path, pdf_path):
    docx_path = os.path.abspath(docx_path)
    pdf_path = os.path.abspath(pdf_path)
    ps = f'''
$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0
try {{
  $doc = $word.Documents.Open("{docx_path}", $false, $true)
  $doc.SaveAs2("{pdf_path}", 17)
  $doc.Close($false)
  Write-Output "converted"
}} finally {{
  $word.Quit()
  [System.Runtime.Interopservices.Marshal]::ReleaseComObject($word) | Out-Null
}}
'''
    r = subprocess.run(["powershell", "-NoProfile", "-NonInteractive", "-Command", ps],
                       capture_output=True, text=True, timeout=300)
    if "converted" not in r.stdout:
        raise RuntimeError(f"Word conversion failed: {r.stdout} {r.stderr}")
    return pdf_path


def pdf_to_pngs(pdf_path, out_dir, dpi=90):
    import fitz
    os.makedirs(out_dir, exist_ok=True)
    doc = fitz.open(pdf_path)
    paths = []
    for i, page in enumerate(doc):
        pix = page.get_pixmap(dpi=dpi)
        p = os.path.join(out_dir, f"page-{i+1:02d}.png")
        pix.save(p)
        paths.append(p)
    doc.close()
    return paths


if __name__ == "__main__":
    docx = sys.argv[1]
    out_dir = sys.argv[2]
    dpi = int(sys.argv[3]) if len(sys.argv) > 3 else 90
    os.makedirs(out_dir, exist_ok=True)
    pdf = os.path.join(out_dir, os.path.splitext(os.path.basename(docx))[0] + ".pdf")
    docx_to_pdf(docx, pdf)
    pages = pdf_to_pngs(pdf, out_dir, dpi)
    print(f"PDF: {pdf}")
    print(f"{len(pages)} pages rendered:")
    for p in pages:
        print(" ", p)
