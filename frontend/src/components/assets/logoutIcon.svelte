<script>
  import { fade } from "svelte/transition";
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<!-- svelte-ignore a11y-no-static-element-interactions -->
<svg
  on:click
  transition:fade={{ duration: 200, delay: 200 }}
  xmlns="http://www.w3.org/2000/svg"
  viewBox="0 0 24 24"
  ><g
    ><path
      d="M12 3.25a.75.75 0 0 1 0 1.5a7.25 7.25 0 0 0 0 14.5a.75.75 0 0 1 0 1.5a8.75 8.75 0 1 1 0-17.5Z"
    /><path
      d="M16.47 9.53a.75.75 0 0 1 1.06-1.06l3 3a.75.75 0 0 1 0 1.06l-3 3a.75.75 0 1 1-1.06-1.06l1.72-1.72H10a.75.75 0 0 1 0-1.5h8.19l-1.72-1.72Z"
    /></g
  ></svg
>

<style>
  svg {
    max-width: var(--size-1);
    min-width: var(--size-1);
    cursor: pointer;
    transform: rotateZ(180deg);
    transition: all ease-in-out var(--dur);
    padding: calc(var(--size-6) * 0.3);
    border-radius: 50%;

    & g {
      fill: var(--bg);

      & path {
        stroke-width: 10;
      }
    }
  }

  svg:hover {
    background-color: var(--main-col-1);
  }
</style>
