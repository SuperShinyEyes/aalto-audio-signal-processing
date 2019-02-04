
# Digital filter
Computational algorithm to modify a digital signal. Frequencies may be either attenuated or amplified.

1. Feedforward FIR filters
2. Feedback IIR filters

## FIR(Finite Impulse Response) filters
### First-Order FIR filter

----------------------------------------------------------------
## IIR(Infinite Impulse Response) filters
The impulse response usually decays exponentially to zero

### One-Pole filter(leaky integrator)

### Allpass filter(IIR)
- Magnitude response is exactly 1 at all frequencies! 
    - Does not attenuate or boost anything...
- Poles & zeros on opposite sides of the unit circle
    - Pole radius R and zero radius 1/R: cancels gain contributions

#### First-Order Allpass filter

#### Applications of Digital Allpass Filters
A lot...

#### Dynamic Range Reduction using an Allpass Filter Chain

----------------------------------------------------------------

## Comb filter
IIR
- Implemented by adding a delayed version of a signal to itself, causing constructive and destructive interference. 
- Can be implemented in both feedforward and feedbackward. 
- When the feedback coefficient is negative, peaks occur at odd harmonics

----------------------------------------------------------------
## Inverse Comb(FIR) filter
Obtained by inverting the comb filter transfer function. Poles become zeros.

----------------------------------------------------------------
## Digital Resonator
### Resonance
- A bump in the magnitude response
    - E.g. a formant, or a mode of a vibrating structure
- Sharpness is described by bandwidth: - Usually, the difference of points where the
gain is 3 dB below the peak
- Other properties:
center frequency & peak value (gain)
- Quality factor:
    - Q = center frequency / bandwidth
    - Large Q value 􏰃 sharp resonance
    - Small Q value 􏰃 wide resonance

### Pole Radius


----------------------------------------------------------------
## Shelving Filter
- Shelving filter is a bass or treble tone control
- Amplifies or attenuates low (high) frequencies without affecting the high (low) ones

### 1st-Order Low Shelf

----------------------------------------------------------------
## Digital Equalizing Filter

----------------------------------------------------------------
## Fractional Delay Filters
- Fractional Delay - Splitting the Unit Delay
- Fractional delay = a delay smaller than sample interval T 
    - Forexample,d=0.5samples
- Fractional delay (FD) is implemented with interpolation
    - In practice, we use digital filters that are called fractional delay filters
    - Discrete-time signals are inherently bandlimited, so the underlying continuous-time signal is known to be smooth between samples
- Acommonuseisalongbutaccuratetimedelay
    - Consists of integral and fractional parts: D = Dint + d

### Application
- Sampling rate conversion
    - Especially conversion between incommensurate rates, e.g., between standard audio sample rates 48 and 44.1 kHz
- Effects & music synthesis using digital waveguides 
    - Comb filters using fractional-length delay lines
- Changing pitch of audio signals
    - Auto-tuning of the singing voice
    - Also, removal of wow from old recordings
- Beamforming using a microphone or loudspeaker array
- Doppler effect in virtual reality
- Wave field synthesis

### FIR Fractional Delay Filters
FIR FD filters have an asymmetric impulse response, but aim at having a linear phase response

### Truncated Sinc Filter

### Lagrange Fractional Delay Filter
#### Linear Interpolation Filter
### Truncated Lagrange Filter

----------------------------------------------------------------
## IIR Fractional Delay Filters


----------------------------------------------------------------
## Thiran Allpass FD Filter


----------------------------------------------------------------
## First-Order Allpass FD Filter

----------------------------------------------------------------
## Conclusion
- Both FIR and IIR filters are useful in audio
- Practical simple filters: leaky integrators, resonators, shelving filters, equalizers, fractional delay filters
- Two types of comb filters: IIR and FIR (inverse)
- Allpass filters are phase equalizers, which are used alone or as building blocks
- Fractional delay filters offer accurate time delays
    - Closer to analog signal processing than DSP usually
    - Often either a Lagrange FIR or a Thiran allpass filter is useful 
    - Try simple things first!