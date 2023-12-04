<script>
  import { dark } from "../../store";
  export let rotate = false;
</script>

<svg
  class:rotate
  xmlns="http://www.w3.org/2000/svg"
  viewBox="0 0 24 24"
  {...$$props}><path class:dark={$dark} d="m12 16l-6-6h12l-6 6Z" /></svg
>

<style>
  svg {
    transition: all ease-in-out 500ms;
    min-width: 1.5rem;
    max-width: 1.5rem;
    cursor: pointer;

    & path {
      transition: all ease-in-out 300ms;
      fill: var(--scroll-color);
    }

    & path.dark {
      fill: var(--icon-active-color);
    }
  }

  svg.rotate {
    transform: rotate(180deg);
  }
</style>
