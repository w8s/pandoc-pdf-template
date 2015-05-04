% Sample Document
% Todd Waits
% May 5, 2015

# pandoc-pdf-template

This repo contains a Latex template file for Pandoc to generated a decent looking PDF right off the bat. If you have any recommendations, or tweaks to make it better, please let me know. I would love to hear from you.

## Dependencies

* pandoc
* A TexLive package.

*Note: On a Mac, I used [BasicTex](http://www.tug.org/mactex/morepackages.html) with the packages below installed using `tlmgr`.*

Tex Packages:

* tocloft
* textpos
* changepage
* titling
* placeins
* lastpage
* sectsty


## Command

`pandoc --latex-engine=xelatex --template={/path/to/w8sPDF.template} -V subject="{subject}" -V keywords="{keywords}" -V today="{today}" -V subtitle="{subtitle}" -V draft="{draft}" -V color="{color}" -V iconpath="path/to/icon.png" -V brandingpath="path/to/brandingfile.eps" -f markdown+auto_identifiers --toc -o "{subtitle}.pdf" {mdfile}"`

## Helper Script

I included a Python script that will run the above command using keywords you define in the script. I find it's a bit easier to use that.
