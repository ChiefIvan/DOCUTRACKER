<script>
  import { dark, navExpand } from "../../store";
  import { tooltip } from "../shared/Tooltip";
</script>

{#if $navExpand}
  <div>
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
      ><path
        d="M16.5 13H15v3.69l3.19 1.84l.75-1.3l-2.44-1.41zM16 9c-1.96 0-3.73.82-5 2.12V7h6l2-2l-2-2h-6V2l-1-1l-1 1v4H3L1 8l2 2h6v10c-1.1 0-2 .9-2 2h5.41c1.05.63 2.28 1 3.59 1c3.87 0 7-3.13 7-7s-3.13-7-7-7m0 11.85c-2.68 0-4.85-2.17-4.85-4.85s2.17-4.85 4.85-4.85s4.85 2.17 4.85 4.85s-2.17 4.85-4.85 4.85"
      /></svg
    >
  </div>
{:else}
  <div
    use:tooltip={{
      arrow: false,
      content: "Update Route",
      animation: "perspective-subtle",
      theme: "tooltip",
      offset: [0, 20],
      placement: "right",
    }}
  >
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
      ><path
        d="M16.5 13H15v3.69l3.19 1.84l.75-1.3l-2.44-1.41zM16 9c-1.96 0-3.73.82-5 2.12V7h6l2-2l-2-2h-6V2l-1-1l-1 1v4H3L1 8l2 2h6v10c-1.1 0-2 .9-2 2h5.41c1.05.63 2.28 1 3.59 1c3.87 0 7-3.13 7-7s-3.13-7-7-7m0 11.85c-2.68 0-4.85-2.17-4.85-4.85s2.17-4.85 4.85-4.85s4.85 2.17 4.85 4.85s-2.17 4.85-4.85 4.85"
      /></svg
    >
  </div>
{/if}

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

    /* & path.bg {
      fill: var(--icon-active-color);
    } */

    /* & path.dark {
      fill: var(--background);
    } */
  }
</style>
