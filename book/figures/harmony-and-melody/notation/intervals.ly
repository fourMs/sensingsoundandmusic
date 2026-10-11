\include "../../notation/common.ily"
% The thirteen intervals from unison to octave above C.
\score {
  <<
    \new Staff { \clef treble \key c \major \omit Staff.TimeSignature \cadenzaOn
      c'2 <c' des'> <c' d'> <c' ees'> <c' e'> <c' f'> <c' fis'> <c' g'> <c' aes'> <c' a'> <c' bes'> <c' b'> <c' c''> \bar "|." }
    \new Lyrics \with { \override LyricText.font-size = #-1 } \lyricmode {
      "P1" "m2" "M2" "m3" "M3" "P4" "A4" "P5" "m6" "M6" "m7" "M7" "P8" }
  >>
  \layout { \context { \Score \override SpacingSpanner.common-shortest-duration = #(ly:make-moment 1/8) } }
}
