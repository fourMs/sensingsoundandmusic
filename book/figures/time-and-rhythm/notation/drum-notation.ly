\include "common.ily"
\score {
  \new DrumStaff \with {
    instrumentName = \markup { \small \column { "hi-hat (x)" "snare" "bass drum" } }
  } {
    \override Score.BarNumber.stencil = ##f
    \numericTimeSignature
    \textLengthOn
    <<
      \new DrumVoice { \voiceOne \drummode {
        \time 4/4
        hh8^\markup { \small "rock beat: eighth-note hi-hat" } hh hh hh hh hh hh hh | hh8 hh hh hh hh hh hh hh \bar "||"
        \break
        \time 12/8 hh4^\markup { \small "shuffle: long–short hi-hat in 12/8" } hh8 hh4 hh8 hh4 hh8 hh4 hh8 \bar "||"
        \break
        \time 4/4 hh16^\markup { \small "funk: sixteenth-note hi-hat" } hh hh hh hh hh hh hh hh hh hh hh hh hh hh hh \bar "|."
      } }
      \new DrumVoice { \voiceTwo \drummode {
        bd4 sn4 bd8 bd8 sn4 | bd4 sn4 bd8 bd8 sn4 |
        bd4. sn4. bd4. sn4. |
        bd4 sn4 bd8 bd8 sn4
      } }
    >>
  }
  \layout { indent = 22\mm }
}
