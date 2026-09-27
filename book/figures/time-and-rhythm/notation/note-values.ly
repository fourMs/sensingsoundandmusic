\include "common.ily"
\score {
  \new RhythmicStaff \with { \omit TimeSignature } {
    \override Score.BarNumber.stencil = ##f
    \textLengthOn
    \time 4/4
    c1^\markup { \small "whole note" } \bar "|"
    c2^\markup { \small "half notes" } c2 \bar "|"
    c4^\markup { \small "quarter notes" } c4 c4 c4 \bar "|"
    \break
    c8^\markup { \small "eighth notes" } c8 c8 c8 c8 c8 c8 c8 \bar "|"
    c16^\markup { \small "sixteenth notes" } c16 c16 c16 c16 c16 c16 c16 c16 c16 c16 c16 c16 c16 c16 c16 \bar "|"
    \break
    r1^\markup { \small "whole rest" } \bar "|"
    r2^\markup { \small "half rest" } r4^\markup { \small "quarter rest" } r8^\markup { \small "eighth rest" } r16^\markup { \small "sixteenth rests" } r16 \bar "|"
    c4.^\markup { \small "dotted quarter" } c8 \tuplet 3/2 { c8^\markup { \small "triplet" } c8 c8 } c4 \bar "|."
  }
  \layout { }
}
