\include "../../notation/common.ily"
% A short melody up and down the C major scale: eighth notes, then a whole note.
\score {
  \new Staff \relative c' { \clef treble \key c \major \time 4/4
    c8 d e f g f e d | c1 \bar "|." }
}
