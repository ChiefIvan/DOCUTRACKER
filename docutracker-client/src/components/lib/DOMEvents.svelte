<script lang="ts">
  import { modeExpand, navExpand, profileExpand, dark } from "../../store";
  let width: number;

  $: $navExpand = width > 500;

  $: {
    $dark
      ? (document.body.className = "dark")
      : (document.body.className = "light");
  }

  const close = (): void => {
    if ($modeExpand) {
      $modeExpand = false;
    }
  };

  const closeProfile = (event: Event): void => {
    const target = event.target as HTMLInputElement;

    if ($profileExpand && target.closest(".profiles") === null) {
      $profileExpand = false;
    }
  };

  const debounce = (
    func: (...args: any[]) => void,
    wait: number
  ): (() => void) => {
    let timeout: number | undefined;
    return function executedFunction(...args: any[]): void {
      const later = (): void => {
        clearTimeout(timeout);
        func(...args);
      };
      clearTimeout(timeout);
      timeout = setTimeout(later, wait);
    };
  };

  const debouncedClose = debounce(close, 100);
</script>

<svelte:window
  bind:innerWidth={width}
  on:scroll={debouncedClose}
  on:resize={debouncedClose}
  on:click={(e) => {
    close();
    closeProfile(e);
  }}
/>
