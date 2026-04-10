# Sensing Sound and Music

This is the source code for the e-book [Sensing Sound and Music](https://fourms.github.io/sensingsoundandmusic/), which contains lecture notes and materials for the [course MUS2640](https://www.uio.no/studier/emner/hf/imv/MUS2640/) at the University of Oslo (UiO). It has been written using [Jupyter Book](https://jupyterbook.org/) v2 and can be compiled to different formats. If you are mainly interested in the content, go to [the build](https://fourms.github.io/sensingsoundandmusic/).  

## How to run locally

To run the book using a local server: 

    cd book
    jupyter book start

To build the HTML version of the book: 

    cd book
    myst build --html

To build both HTML and the LaTeX-based PDF:

    cd book
    myst build --all

The PDF requires a working LaTeX installation. On Debian/Ubuntu:

    sudo apt-get install texlive-latex-extra texlive-fonts-extra \
        texlive-fonts-recommended texlive-science texlive-xetex latexmk lmodern

The generated PDF is written to `book/_build/exports/sensing-sound-and-music.pdf`.

## Credits

Alexander Refsum Jensenius, Guilherme Schmidt Camara, Sara D'Amario, Laura Bishop.