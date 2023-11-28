<script>
  export let compColor = false;
</script>

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
  ><path
    class:bg={compColor}
    d="M3 19q-.825 0-1.412-.587T1 17V7q0-.825.588-1.412T3 5h10q.825 0 1.413.588T15 7v10q0 .825-.587 1.413T13 19zm14 0V5h2v14zm4 0V5h2v14z"
  /></svg
>

<style>
  svg {
    min-width: 2rem;
    max-width: 2rem;
    cursor: pointer;
    transition: all ease-in-out 500ms;

    & path {
      transition: all ease-in-out 500ms;
      fill: var(--main-col-1);
    }

    & path.bg {
      fill: var(--main-col-1);
    }

    /* & path.bg {
      fill: var(--icon-active-color);
    } */

    /* & path.dark {
      fill: var(--background);
    } */
  }
</style>
