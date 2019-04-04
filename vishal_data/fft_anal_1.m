load data.mat;
sig = sig(1251:2500);
Ts = 2*10^-3;
Fs = 1/Ts;
Fnyq = Fs/2;
t = 0:Ts:(1250-1)*Ts;

Fpass = 35; % passband cutoff 35 Hz
Fstop = 45; % stopband cutoff 45 Hz

wp_normalised = Fpass/Fnyq; % normalised wp
ws_normalised = Fstop/Fnyq; % normalised ws

f = [0 wp_normalised ws_normalised 1]; % significant normalised freq
a = [1 1 0 0]; % desired amplitudes

coeff = firpm(100,f,a); % filter coefficients returned for order 100
sig = filter(coeff,1,sig);

figure(1);
plot(t, sig);
grid on;
xlabel("Time");
ylabel("Signal");
SIG = fft(sig);
freq = linspace(0, Fs/2, 1250/2);
figure(2);
plot(freq, abs(SIG(1:625)));
grid on;
xlabel ("Frequency (in Hz)");
ylabel("Strength");

