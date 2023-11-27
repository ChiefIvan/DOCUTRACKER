<script>
  import { dark } from "../../store";
</script>

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
  ><path
    class:bg={$dark}
    fill="currentColor"
    d="M13 9h5l-5-5v5ZM6 22q-.825 0-1.413-.588T4 20v-3h16v3q0 .825-.588 1.413T18 22H6Zm-5-7v-2h22v2H1Zm3-4V4q0-.825.588-1.413T6 2h8l6 6v3H4Z"
  /></svg
>

<style>
  svg {
    min-width: 1.8rem;
    max-width: 1.8rem;
    cursor: pointer;
    transition: all ease-in-out 500ms;

    & path {
      transition: all ease-in-out 500ms;
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
