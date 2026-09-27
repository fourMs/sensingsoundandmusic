\include "common.ily"
\score {
  \new RhythmicStaff {
    \override Score.BarNumber.stencil = ##f
    \numericTimeSignature
    \textLengthOn
    \time 2/4 c8->[^\markup { \small "2/4: two beats" } c8] c8->[ c8] \bar "||"
    \time 3/4 c8->[^\markup { \small "3/4: three beats" } c8] c8->[ c8] c8->[ c8] \bar "||"
    \time 4/4 c8->[^\markup { \small "4/4: four beats" } c8] c8->[ c8] c8->[ c8] c8->[ c8] \bar "||"
    \break
    \time 6/8 c8->[^\markup { \small "6/8: two beats of three (3+3)" } c8 c8] c8->[ c8 c8] \bar "||"
    \time 7/8 c8->[^\markup { \small "7/8: three unequal beats (2+2+3)" } c8] c8->[ c8] c8->[ c8 c8] \bar "||"
    \time 5/4 c4->^\markup { \small "5/4: five beats" } c4 c4-> c4 c4 \bar "|."
  }
  \layout { }
}
