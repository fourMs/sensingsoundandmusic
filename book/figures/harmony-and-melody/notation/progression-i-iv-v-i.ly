\include "../../notation/common.ily"
% The I–IV–V–I progression in C major.
\score {
  <<
    \new ChordNames \chordmode { c1 f g c }
    \new Staff { \clef treble \key c \major \time 4/4
      <c' e' g'>1 <f' a' c''> <g' b' d''> <c' e' g'> \bar "|." }
    \new Lyrics \lyricmode { I IV V I }
  >>
  \layout { \context { \Score \override SpacingSpanner.common-shortest-duration = #(ly:make-moment 1/16) \override SpacingSpanner.spacing-increment = #2.4 } }
}
