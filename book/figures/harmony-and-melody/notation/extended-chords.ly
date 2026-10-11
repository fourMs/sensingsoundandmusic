\include "../../notation/common.ily"
% Extended chords on C: the seventh, ninth, eleventh, and thirteenth.
\score {
  <<
    \new Staff { \clef treble \key c \major \time 4/4
      <c' e' g' bes'>1^"C7" <c' e' g' bes' d''>^"C9" <c' e' g' bes' d'' f''>^"C11" <c' e' g' bes' d'' f'' a''>^"C13" \bar "|." }
    
  >>
  \layout { \context { \Score \override SpacingSpanner.common-shortest-duration = #(ly:make-moment 1/16) \override SpacingSpanner.spacing-increment = #2.4 } }
}
