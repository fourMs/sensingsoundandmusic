# Sensing Sound and Music

This is the source code for the e-book [Sensing Sound and Music](https://fourms.github.io/sensingsoundandmusic/), which contains lecture notes and materials for the [course MUS2640](https://www.uio.no/studier/emner/hf/imv/MUS2640/) at the University of Oslo (UiO). The course is primarily targeting music students, introducing basic concepts in music psychology and music technology. The integration of psychology and technology is not so common, so this book is meant to bridge the gap between two sets of literature that are often separated. 

The book is exploring the potential of new technologies in educational material. It has been written using [Jupyter Book](https://jupyterbook.org/) v2 and can be compiled to different formats. The use of Jupyter notebooks support inline code and figures. The book also experiments with using WebAudio-based web pages for examples. 

Since teaching is ongoing, the material is also changing based on things that happen in class, student questions, etc. So keep returning. If you are mainly interested in the content, go to [the build](https://fourms.github.io/sensingsoundandmusic/). 

## How to run locally

To run the book using a local server: 

    cd book
    jupyter book start

To build the HTML version of the book: 

    cd book
    myst build --html

For a full local build with executed notebooks (as in CI), use:

    cd book
    myst build --html --execute

Or from the repository root:

    ./scripts/verify-book-build.sh

### Run notebook execution before every push (optional)

CI already runs `myst build --html --execute` on `main`. To run the same check locally before `git push`, enable this repository’s hooks once:

    git config core.hooksPath .githooks

To push without the check (e.g. a docs-only WIP branch):

    SKIP_BOOK_VERIFY=1 git push

## Credits

Alexander Refsum Jensenius, Guilherme Schmidt Camara, Sara D'Amario, Laura Bishop. AI support by Claude, Cursor, CoPilot, NotebookLM, Gemini.