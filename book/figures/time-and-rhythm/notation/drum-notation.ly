\include "common.ily"
\paper { score-system-spacing.basic-distance = #9 }
lay = \layout {
  indent = 30\mm
  \context { \Score \override SpacingSpanner.spacing-increment = #1.3 }
  \context { \DrumStaff \consists "Instrument_name_engraver" }
}
pattern = #(define-music-function (name hats lower) (markup? ly:music? ly:music?)
  #{
    \new DrumStaff \with { instrumentName = $name } {
      \override Score.BarNumber.stencil = ##f
      \numericTimeSignature
      <<
        \new DrumVoice { \voiceOne $hats }
        \new DrumVoice { \voiceTwo $lower }
      >>
    }
  #})
\score {
  \pattern \markup { \small \column { "Rock beat" "eighth-note hi-hat" } }
    \drummode { \time 4/4 hh8 hh hh hh hh hh hh hh | hh8 hh hh hh hh hh hh hh \bar "|." }
    \drummode { bd4 sn4 bd8 bd8 sn4 | bd4 sn4 bd8 bd8 sn4 }
  \layout { \lay }
}
\score {
  \pattern \markup { \small \column { "Shuffle" "long–short hi-hat in 12/8" } }
    \drummode { \time 12/8 hh4 hh8 hh4 hh8 hh4 hh8 hh4 hh8 | hh4 hh8 hh4 hh8 hh4 hh8 hh4 hh8 \bar "|." }
    \drummode { bd4. sn4. bd4. sn4. | bd4. sn4. bd4. sn4. }
  \layout { \lay }
}
\score {
  \pattern \markup { \small \column { "Funk" "sixteenth-note hi-hat" } }
    \drummode { \time 4/4 hh16 hh hh hh hh hh hh hh hh hh hh hh hh hh hh hh | hh16 hh hh hh hh hh hh hh hh hh hh hh hh hh hh hh \bar "|." }
    \drummode { bd4 sn4 bd8 bd8 sn4 | bd4 sn4 bd8 bd8 sn4 }
  \layout { \lay }
}
