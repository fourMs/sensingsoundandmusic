\include "common.ily"
row = #(define-music-function (name notes rests) (markup? ly:music? ly:music?)
  #{
    \new RhythmicStaff \with {
      instrumentName = $name
      \omit TimeSignature
    } {
      \override Score.BarNumber.stencil = ##f
      \time 4/4
      $notes \bar "|" $rests \bar "|"
    }
  #})
\score {
  <<
    \row \markup { \small "whole (semibreve)" } { c1 } { r1 }
    \row \markup { \small "half (minim)" } { c2 c2 } { r2 r2 }
    \row \markup { \small "quarter (crotchet)" } { c4 c4 c4 c4 } { r4 r4 r4 r4 }
    \row \markup { \small "eighth (quaver)" } { c8[ c8] c8[ c8] c8[ c8] c8[ c8] } { r8 r8 r8 r8 r8 r8 r8 r8 }
    \row \markup { \small "sixteenth (semiquaver)" } { c16[ c16 c16 c16] c16[ c16 c16 c16] c16[ c16 c16 c16] c16[ c16 c16 c16] } { r16 r16 r16 r16 r16 r16 r16 r16 r16 r16 r16 r16 r16 r16 r16 r16 }
    \row \markup { \small "dotted and triplet" } { c4. c8 \tuplet 3/2 { c8[ c8 c8] } c4 } { r4. r8 \tuplet 3/2 { r8 r8 r8 } r4 }
  >>
  \layout {
    indent = 34\mm
    \context {
      \Score
      proportionalNotationDuration = #(ly:make-moment 1/16)
      \override SpacingSpanner.uniform-stretching = ##t
      \override SpacingSpanner.strict-note-spacing = ##t
    }
    \context { \RhythmicStaff \override VerticalAxisGroup.staff-staff-spacing.basic-distance = #7 }
  }
}
