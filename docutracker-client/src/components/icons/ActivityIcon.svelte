<script>
  import { dark } from "../../store";
  export let compColor = false;
  export let medium = false;
</script>

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
  ><path
    class:dark={$dark}
    class:bg={compColor}
    d="m19.65 20.35l.7-.7l-1.85-1.85V15h-1v3.2l2.15 2.15ZM10 6h4V4h-4v2Zm8 17q-2.075 0-3.538-1.463T13 18q0-2.075 1.463-3.538T18 13q2.075 0 3.538 1.463T23 18q0 2.075-1.463 3.538T18 23ZM2 21V6h6V2h8v4h6v6.275q-.875-.625-1.9-.95T18 11q-2.9 0-4.95 2.05T11 18q0 .775.163 1.538T11.675 21H2Z"
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
    }

    & path.bg {
      fill: var(--icon-active-color);
    }

    & path.dark {
      fill: var(--background);
    }
  }
</style>
