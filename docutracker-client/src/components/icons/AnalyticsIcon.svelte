<script>
  export let compColor = false;
</script>

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
  ><path
    class:active={compColor}
    d="M15.86 4.39v15c0 1.67 1.14 2.61 2.39 2.61c1.14 0 2.39-.79 2.39-2.61V4.5c0-1.54-1.14-2.5-2.39-2.5s-2.39 1.06-2.39 2.39M9.61 12v7.39C9.61 21.07 10.77 22 12 22c1.14 0 2.39-.79 2.39-2.61v-7.28c0-1.54-1.14-2.5-2.39-2.5S9.61 10.67 9.61 12m-3.86 5.23c1.32 0 2.39 1.07 2.39 2.38a2.39 2.39 0 1 1-4.78 0c0-1.31 1.07-2.38 2.39-2.38"
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

    & path.active {
      fill: var(--icon-active-color);
    }

    /* & path.bg {
      fill: var(--icon-active-color);
    } */

    /* & path.dark {
      fill: var(--background);
    } */
  }
</style>
