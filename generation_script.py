from subprocess import Popen, PIPE, STDOUT
import shlex
import glob


template_path = "w8sPDF.template"
subject = "Subject of PDF"
keywords = "Keywords, You, Want, To, Include"
subtitle = "The Name of the Document" # Acts as name of document as well.
color = "102,103,150" # RGB color for links inside the document.
today = "05/06/2015"
draft = "1.0" # Text that will be appended to "Version" in the document. i.e
              # Version 1.0, or Version DRAFT.
iconpath="256x256.png"
brandingpath="400x50.png"

mdfiles = glob.glob1(".", "*.md")
mdfile = ' '.join(mdfiles)

pandoc = ("pandoc --latex-engine=xelatex "
          "--template={template_path}"
          " -V subject=\"{subject}\" -V keywords=\"{keywords}\""
          " -V today=\"{today}\" -V subtitle=\"{subtitle}\""
          " -V draft=\"{draft}\" -V color=\"{color}\""
          " -V iconpath=\"{iconpath}\" -V brandingpath=\"{brandingpath}\""
          " -f markdown+auto_identifiers --toc -o \"{subtitle}.pdf\" {mdfile} "
          )

process = Popen(shlex.split(pandoc.format(**locals())),
                stdin=PIPE, stdout=PIPE, stderr=STDOUT, shell=False)

process.wait()

if(process.returncode != 0) :
    text = str(process.communicate())
    err = "Could not generate %s.pdf! \n%s']" % (subtitle, text)
    print err;
else :
    out = "Generated %s.pdf" % subtitle
    print out
