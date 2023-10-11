<script>
  import { dark } from "../../stores";

  export let arrowState = false;
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<!-- svelte-ignore a11y-no-static-element-interactions -->
<svg
  on:click
  class:rotate={arrowState}
  xmlns="http://www.w3.org/2000/svg"
  viewBox="0 0 24 24"
  ><path
    class:dark={$dark}
    d="M8.59 16.59L13.17 12L8.59 7.41L10 6l6 6l-6 6l-1.41-1.41z"
  /></svg
>

<style>
  svg {
    max-width: var(--size-1);
    min-width: var(--size-1);
    cursor: pointer;
    transform: rotateZ(540deg);
    transition: all ease-in-out var(--dur);
    border-radius: 50%;

    & path {
      fill: var(--main-col-1);
      transition: all ease-in-out var(--dur);
    }

    & path.dark {
      fill: var(--bg);
    }
  }

  svg:hover {
    background-color: var(--main-col-1);
  }

  svg:hover path {
    fill: var(--bg);
  }

  svg.rotate {
    transform: rotateZ(0);
  }

  /* svg:hover {
    opacity: 0.6;
  } */
</style>
