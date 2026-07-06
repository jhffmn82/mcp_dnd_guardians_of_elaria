# montage.py <docx> <outdir>  -> renders + builds a thumbnail montage for layout QA
import sys, os, glob, subprocess
sys.path.insert(0, os.path.dirname(__file__))
import render_check
from PIL import Image, ImageDraw
docx, outdir = sys.argv[1], sys.argv[2]
os.makedirs(outdir, exist_ok=True)
pdf = os.path.join(outdir, os.path.splitext(os.path.basename(docx))[0] + ".pdf")
render_check.docx_to_pdf(docx, pdf)
render_check.pdf_to_pngs(pdf, outdir, 60)
pages = sorted(glob.glob(outdir + "/page-*.png"))
TW=250; cols=6; rows=(len(pages)+cols-1)//cols; TH=int(TW*11/8.5)
sheet=Image.new('RGB',(cols*TW, rows*(TH+16)),'gray'); dr=ImageDraw.Draw(sheet)
for i,p in enumerate(pages):
    im=Image.open(p).convert('RGB'); im.thumbnail((TW,TH))
    x,y=(i%cols)*TW,(i//cols)*(TH+16); sheet.paste(im,(x,y)); dr.text((x+3,y+TH+2),f"p{i+1}",fill='white')
out=outdir+"/_montage.png"; sheet.save(out)
print("PAGES", len(pages)); print("MONTAGE", out)
