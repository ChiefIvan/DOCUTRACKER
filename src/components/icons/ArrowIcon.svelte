<script lang="ts">
  import { tooltip } from "../shared/Tooltip";

  export let arrowState = false;
  export let sizeMedium = false;
  export let dark = false;
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<!-- svelte-ignore a11y-no-static-element-interactions -->
<svg
  on:click|stopPropagation
  class:rotate={arrowState}
  class:medium={sizeMedium}
  xmlns="http://www.w3.org/2000/svg"
  viewBox="0 0 24 24"
>
  <path
    class:dark
    d="M8.59 16.59L13.17 12L8.59 7.41L10 6l6 6l-6 6l-1.41-1.41z"
  /></svg
>

<style>
  svg {
    width: 1.5rem;
    height: 1.5rem;
    cursor: pointer;
    transition: all ease-in-out 500ms;
    border-radius: 50%;

    & path {
      fill: var(--main-col-1);
      transition: all ease-in-out 500ms;
    }

    & path.dark {
      fill: var(--background);
    }
  }

  svg:hover {
    background-color: var(--main-col-7);
  }

  svg:hover path {
    fill: var(--background);
  }

  svg.rotate {
    transform: rotateZ(180deg);
  }

  /* svg:hover {
    opacity: 0.6;
  } */

  svg.medium {
    width: 1.8rem;
    height: 1.8rem;
  }
</style>
