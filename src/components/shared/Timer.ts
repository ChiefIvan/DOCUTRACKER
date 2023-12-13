import { writable } from "svelte/store";

export class Timer {
  private countdown: any;
  public timeLeft: any;
  private timerkey: string;

  constructor() {
    this.timerkey = "";
    this.timeLeft = writable(0);
  }

  subscribe(run: (value: number) => void) {
    return this.timeLeft.subscribe(run);
  }

  startTimer(duration: number, key: string) {
    this.timeLeft.set(duration);
    this.timerkey = key;

    localStorage.setItem(this.timerkey, Date.now().toString());

    this.countdown = setInterval(() => {
      this.timeLeft.update((value: number) => {
        if (value > 0) {
          return value - 1;
        } else {
          clearInterval(this.countdown);
          return 0;
        }
      });
    }, 1000);
  }

  checkTimer(delay: number, key: string) {
    this.timerkey = key;

    const storedResendTime = localStorage.getItem(this.timerkey);
    if (storedResendTime) {
      const elapsedTime = Date.now() - Number(storedResendTime);

      if (elapsedTime < delay) {
        this.timeLeft.set(Math.ceil((delay - elapsedTime) / 1000));

        this.countdown = setInterval(() => {
          this.timeLeft.update((value: number) => {
            if (value > 0) {
              return value - 1;
            } else {
              clearInterval(this.countdown);
              return 0;
            }
          });
        }, 1000);
      }
    }
  }
}
