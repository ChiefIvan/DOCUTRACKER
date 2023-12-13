<script>
  import { dark } from "../../store";
  export let compColor = false;
  export let medium = false;
</script>

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
  ><path
    class:dark={$dark}
    class:bg={compColor}
    stroke-linecap="round"
    stroke-linejoin="round"
    stroke-width="2"
    d="M4 4h6v8H4zm0 12h6v4H4zm10-4h6v8h-6zm0-8h6v4h-6z"
  /></svg
>

<style>
  svg {
    min-width: 2rem;
    max-width: 2rem;
    cursor: pointer;
    transition: all ease-in-out 500ms;

    & path {
      transition: all ease-in-out 300ms;
      fill: var(--main-col-1);
      stroke: var(--main-col-1);
    }

    & path.bg {
      fill: var(--icon-active-color);
      stroke: var(--icon-active-color);
    }

    & path.dark {
      stroke: var(--background);
      fill: var(--background);
    }
  }
</style>
