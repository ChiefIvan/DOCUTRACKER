<script>
  import { dark, navExpand } from "../../store";
  import { tooltip } from "../shared/Tooltip";

  export let active = false;
</script>

{#if $navExpand}
  <div>
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
      ><path
        class:dark={$dark}
        class:active
        d="M17.5 21h1v-2.5H21v-1h-2.5V15h-1v2.5H15v1h2.5V21Zm.5 2q-2.075 0-3.538-1.463T13 18q0-2.075 1.463-3.538T18 13q2.075 0 3.538 1.463T23 18q0 2.075-1.463 3.538T18 23ZM7 9h10V7H7v2Zm4.675 12H5q-.825 0-1.413-.588T3 19V5q0-.825.588-1.413T5 3h14q.825 0 1.413.588T21 5v6.7q-.725-.35-1.463-.525T18 11q-.275 0-.513.012t-.487.063V11H7v2h6.125q-.45.425-.813.925T11.675 15H7v2h4.075q-.05.25-.063.488T11 18q0 .825.15 1.538T11.675 21Z"
      /></svg
    >
  </div>
{:else}
  <div
    use:tooltip={{
      arrow: false,
      content: "Register Document",
      animation: "perspective-subtle",
      theme: "tooltip",
      offset: [0, 20],
      placement: "right",
    }}
  >
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
      ><path
        class:dark={$dark}
        class:active
        d="M17.5 21h1v-2.5H21v-1h-2.5V15h-1v2.5H15v1h2.5V21Zm.5 2q-2.075 0-3.538-1.463T13 18q0-2.075 1.463-3.538T18 13q2.075 0 3.538 1.463T23 18q0 2.075-1.463 3.538T18 23ZM7 9h10V7H7v2Zm4.675 12H5q-.825 0-1.413-.588T3 19V5q0-.825.588-1.413T5 3h14q.825 0 1.413.588T21 5v6.7q-.725-.35-1.463-.525T18 11q-.275 0-.513.012t-.487.063V11H7v2h6.125q-.45.425-.813.925T11.675 15H7v2h4.075q-.05.25-.063.488T11 18q0 .825.15 1.538T11.675 21Z"
      /></svg
    >
  </div>
{/if}

<style>
  div {
    display: flex;
    align-items: center;

    & svg {
      min-width: 1.8rem;
      max-width: 1.8rem;
      cursor: pointer;
      transition: all ease-in-out 500ms;

      & path {
        transition: all ease-in-out 500ms;
        fill: var(--main-col-1);
      }

      & path.dark {
        fill: var(--icon-dark);
      }

      & path.active {
        fill: var(--icon-active-color);
      }
    }
  }
</style>
