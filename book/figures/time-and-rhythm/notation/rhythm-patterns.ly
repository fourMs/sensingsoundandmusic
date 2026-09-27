\include "common.ily"
\score {
  <<
    \new RhythmicStaff \with { instrumentName = \markup { \small "tresillo 3+3+2" } } {
      \override Score.BarNumber.stencil = ##f
      \numericTimeSignature
      \time 4/4 c4. c4. c4 | c4. c4. c4 \bar "|."
    }
    \new RhythmicStaff \with { instrumentName = \markup { \small "3+3+3+3+2+2" } } {
      c8. c8. c8. c8. c8 c8 | c8. c8. c8. c8. c8 c8
    }
    \new RhythmicStaff \with { instrumentName = \markup { \small "cinquillo" } } {
      c4 c8 c4 c8 c4 | c4 c8 c4 c8 c4
    }
    \new RhythmicStaff \with { instrumentName = \markup { \small "son clave (3–2)" } } {
      c8. c8. c8 r8 r4 | r4 c8 c8 r4
    }
  >>
  \layout { indent = 28\mm }
}
