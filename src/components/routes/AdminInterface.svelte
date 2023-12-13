<script lang="ts">
  import { afterUpdate, onMount } from "svelte";
  import { navigate } from "svelte-routing";
  import {
    adminUser,
    handleFetch,
    address,
    dark,
    type RequestAPI,
    type ResponseData,
    activeDocument,
  } from "../../store";

  import TriangleIcon from "../icons/TriangleIcon.svelte";
  import Button from "../shared/Button.svelte";

  let request: ResponseData;
  let activeRoute = "";
  let locationExpand = false;
  let filtered_documents: Array<{ user: any; approved: boolean }> = [];

  const genRequest: RequestAPI = {
    method: "GET",
    address: `${address}/get_all`,
  };

  onMount(async () => {
    if ($adminUser !== "Ban") {
      navigate("/admin/login");
    }

    request = await handleFetch(genRequest);
  });

  function filterDocuments() {
    filtered_documents = [];

    if (request && request.users) {
      request.users.forEach((user) => {
        user.documents.forEach((document) => {
          document.documentPath.forEach((route) => {
            if (route.name === activeRoute) {
              filtered_documents.push({
                user,
                approved: route.approved,
              });
            }
          });
        });
      });
    }
  }

  // Run the filterDocuments function initially and whenever activeRoute changes
  $: filterDocuments();

  $: console.log(activeRoute);

  const handleApprove = async (user: any) => {
    // Perform approval logic here
    console.log("Approving user:", user);
    // Refresh data after approval
    request = await handleFetch(genRequest);
  };
</script>

<main>
  <!-- svelte-ignore a11y-click-events-have-key-events -->
  <!-- svelte-ignore a11y-no-static-element-interactions -->
  <div
    class="location-wrapper"
    on:click|stopPropagation={() => (locationExpand = !locationExpand)}
  >
    {#if activeRoute.length}
      {#if request && request.routes}
        {#each request.routes as route}
          {#if activeRoute === route}
            <span class="location-active"> {route} </span>
          {/if}
        {/each}
      {/if}
    {:else}
      <span class="location-active"> Please Select a Location </span>
    {/if}
    <TriangleIcon></TriangleIcon>
  </div>
  <div
    class="expand-wrapper"
    class:wrapper-expand={locationExpand}
    class:dark={$dark}
  >
    <ul class="wrapper">
      {#if request && request.routes}
        {#each request.routes as route}
          <!-- svelte-ignore a11y-click-events-have-key-events -->
          <!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
          <li
            on:click={() => {
              activeRoute = route;
              locationExpand = false;
            }}
          >
            <span class="name" class:active={activeRoute === route}
              >{route}</span
            >
          </li>
        {/each}
      {/if}
    </ul>
  </div>
  <div class="card-wrapper">
    {#if filtered_documents.length > 0}
      {#each filtered_documents as { user, approved }}
        {#if !approved}
          <div class="card">
            <img src={`data:image/png;base64,${user.userImg}`} alt="" />
            {user.firstName}
            <Button on:click={() => handleApprove(user)}>Approve</Button>
          </div>
        {/if}
      {/each}
    {:else}
      <p>No documents to display.</p>
    {/if}
  </div>
</main>

<style>
  main {
    & div.location-wrapper {
      margin: 0.5rem;
      width: fit-content;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 0.5rem 1rem;
      border: 1px solid var(--header-color);
      cursor: pointer;
      border-radius: 5rem;
    }

    & div.expand-wrapper {
      display: grid;
      grid-template-rows: 0fr;

      overflow: hidden;
      position: fixed;
      top: 6.5rem;
      left: 0.5rem;
      z-index: 1;

      transition: all ease-in-out 400ms;
      background-color: var(--background);
      box-shadow: 5px 5px 25px lightgray;
      border-radius: 0.5rem;
      box-shadow: 2px 3px 5px rgba(0, 0, 0, 0.3);

      & ul.wrapper {
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

          & span.name {
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

    & div.wrapper-expand {
      grid-template-rows: 1fr;
    }

    & div.dark {
      background-color: var(--dark-main-col-1);
      box-shadow: none;
    }

    & div.card-wrapper {
      margin-top: 3rem;
      padding: 1rem;
      display: grid;
      column-gap: 1rem;
      row-gap: 3.5rem;
      grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr));

      & div.card {
        display: flex;
        align-items: center;
        flex-direction: column;
        justify-content: flex-end;
        background-color: var(--header-color);
        height: 10rem;
        border-radius: 0.5rem;
        cursor: pointer;
        position: relative;
        padding: 0.5rem;

        & img {
          position: absolute;
          width: 5rem;
          height: 5rem;
          top: -2.5rem;
          left: 50%;
          transform: translate(-50%);
          border-radius: 50%;
        }
      }

      /* & div.card > * {
        margin-bottom: 0.5rem;
      } */
    }
  }
</style>
