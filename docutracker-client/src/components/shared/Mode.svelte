<script lang="ts">
  import { beforeUpdate } from "svelte";
  import {
    modeExpand,
    dark,
    profileExpand,
    location,
    notificationExpand,
  } from "../../store";
  import { tooltip } from "./Tooltip";

  import SunIcon from "../icons/SunIcon.svelte";
  import MoonIcon from "../icons/MoonIcon.svelte";
  import SystemIcon from "../icons/SystemIcon.svelte";

  let mode: string | null;

  beforeUpdate(() => {
    mode = localStorage.getItem("mode");
    mode !== "System"
      ? mode !== "Dark"
        ? ($dark = false)
        : ($dark = true)
      : !window.matchMedia("(prefers-color-scheme: dark)").matches
        ? ($dark = false)
        : ($dark = true);
  });

  const enableLight = () => {
    localStorage.setItem("mode", "Light");
    $modeExpand = false;
  };

  const enableDark = () => {
    localStorage.setItem("mode", "Dark");
    $modeExpand = false;
  };

  const enableSystem = () => {
    localStorage.setItem("mode", "System");
    $modeExpand = false;
  };

  const modes = [
    { id: 1, modeName: "Light", comp: SunIcon, bind: enableLight },
    { id: 2, modeName: "Dark", comp: MoonIcon, bind: enableDark },
    { id: 3, modeName: "System", comp: SystemIcon, bind: enableSystem },
  ];

  const openModes = () => {
    $modeExpand = !$modeExpand;
    $profileExpand = false;
    $notificationExpand = false;
  };
</script>

{#each modes as value (value.id)}
  <!-- svelte-ignore a11y-click-events-have-key-events -->
  <!-- svelte-ignore a11y-no-static-element-interactions -->

  {#if value.modeName === mode}
    {#if !$modeExpand}
      <div
        use:tooltip={{
          arrow: false,
          content: "Modes",
          animation: "perspective-subtle",
          theme: "tooltip",
          offset: [0, 20],
          placement: "bottom",
        }}
        class="comp-render"
        on:click|stopPropagation={openModes}
      >
        <svelte:component this={value.comp} active={true} />
      </div>
    {:else}
      <div class="comp-render" on:click|stopPropagation={openModes}>
        <svelte:component this={value.comp} active={true} />
      </div>
    {/if}
  {/if}
{/each}

<div
  class="comp-wrapper"
  class:wrapper-expand={$modeExpand}
  class:dark={$dark}
  class:outside={$location === "/" || $location === "/admin"}
>
  <ul class="mode-wrapper">
    {#each modes as value (value.id)}
      <!-- svelte-ignore a11y-click-events-have-key-events -->
      <!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
      <li on:click={value.bind}>
        <svelte:component
          this={value.comp}
          active={value.modeName === mode && true}
        />
        <span class="mode-name" class:active={value.modeName === mode && true}
          >{value.modeName}</span
        >
      </li>
    {/each}
  </ul>
</div>

<style>
  .comp-render {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .comp-wrapper {
    display: grid;
    grid-template-rows: 0fr;

    overflow: hidden;
    position: fixed;
    top: 3.5rem;
    right: 2.5rem;
    z-index: 1;

    transition: all ease-in-out 400ms;
    background-color: var(--background);
    box-shadow: 5px 5px 25px lightgray;
    border-radius: 0.5rem;
    box-shadow: 2px 3px 5px rgba(0, 0, 0, 0.3);

    & ul.mode-wrapper {
      min-height: 0;

      & li {
        display: flex;
        align-items: center;
        column-gap: 0.5rem;
        margin: 0.2rem;
        padding: 0.2rem 0.5rem;
        border-radius: 0.4rem;
        transition: all ease-in-out 500ms;
        cursor: pointer;

        & span.mode-name {
          color: var(--main-col-1);
        }

        & span.active {
          color: var(--icon-active-color);
        }
      }

      & li:hover {
        background-color: var(--main-col-2);
      }
    }
  }

  div.outside {
    right: 0.5rem;
  }

  div.wrapper-expand {
    grid-template-rows: 1fr;
  }

  div.dark {
    background-color: var(--dark-main-col-1);
    box-shadow: none;
  }
</style>
