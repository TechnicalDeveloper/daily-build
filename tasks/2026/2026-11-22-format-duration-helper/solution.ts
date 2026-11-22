export interface DurationParts {
  days: number;
  hours: number;
  minutes: number;
  seconds: number;
}

export function parseDuration(totalSeconds: number): DurationParts {
  if (totalSeconds < 0) throw new Error("Duration cannot be negative");
  if (!Number.isFinite(totalSeconds)) throw new Error("Duration must be a finite number");
  const total = Math.floor(totalSeconds);
  const days = Math.floor(total / 86400);
  const hours = Math.floor((total % 86400) / 3600);
  const minutes = Math.floor((total % 3600) / 60);
  const seconds = total % 60;
  return { days, hours, minutes, seconds };
}

export function formatDuration(totalSeconds: number): string {
  const parts = parseDuration(totalSeconds);
  const units: Array<[number, string]> = [
    [parts.days, "d"],
    [parts.hours, "h"],
    [parts.minutes, "m"],
    [parts.seconds, "s"],
  ];
  const str = units
    .filter(([value]) => value > 0)
    .map(([value, unit]) => `${value}${unit}`)
    .join(" ");
  return str === "" ? "0s" : str;
}
