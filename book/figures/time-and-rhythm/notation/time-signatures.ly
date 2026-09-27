\include "common.ily"
\paper { score-system-spacing.basic-distance = #10 }
row = #(define-music-function (name music) (markup? ly:music?)
  #{
    \new RhythmicStaff \with { instrumentName = $name } {
      \override Score.BarNumber.stencil = ##f
      \numericTimeSignature
      $music \bar "|"
    }
  #})
lay = \layout {
  indent = 50\mm
  \context {
    \Score
    proportionalNotationDuration = #(ly:make-moment 1/8)
    \override SpacingSpanner.uniform-stretching = ##t
    \override SpacingSpanner.strict-note-spacing = ##t
  }
}
\score { \row \markup { \small "2/4: two beats" } { \time 2/4 c8->[ c8] c8->[ c8] } \layout { \lay } }
\score { \row \markup { \small "3/4: three beats" } { \time 3/4 c8->[ c8] c8->[ c8] c8->[ c8] } \layout { \lay } }
\score { \row \markup { \small "4/4: four beats" } { \time 4/4 c8->[ c8] c8->[ c8] c8->[ c8] c8->[ c8] } \layout { \lay } }
\score { \row \markup { \small "5/4: five beats" } { \time 5/4 c8->[ c8] c8->[ c8] c8->[ c8] c8->[ c8] c8->[ c8] } \layout { \lay } }
\score { \row \markup { \small "6/8: two beats of three (3+3)" } { \time 6/8 c8->[ c8 c8] c8->[ c8 c8] } \layout { \lay } }
\score { \row \markup { \small "7/8: three unequal beats (2+2+3)" } { \time 7/8 c8->[ c8] c8->[ c8] c8->[ c8 c8] } \layout { \lay } }
