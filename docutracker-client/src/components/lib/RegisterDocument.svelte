<script lang="ts">
  import {
    dark,
    handleFetch,
    address,
    showMessage,
    routeExpand,
    type ResponseData,
    type RequestAPI,
  } from "../../store";
  import { v4 as uuidv4 } from "uuid";
  import { fade } from "svelte/transition";

  import Input from "../shared/Input.svelte";
  import QrCode from "svelte-qrcode";
  import Button from "../shared/Button.svelte";
  import TriangleIcon from "../icons/TriangleIcon.svelte";

  let placeholderHovered = false;
  let qrCodeElement: any;

  export let authToken = "";
  export let fullname: {
    firstName: string;
    middleName: string;
    lastName: string;
  };

  const date = new Date().toLocaleDateString("en-US", {
    weekday: "long",
    year: "numeric",
    month: "long",
    day: "numeric",
  });

  let value: string;

  const handleGenerate = () => {
    if (!documentName.length) {
      $showMessage = { error: "Please fill all entries first" };
      return;
    }

    if (!documentDescription.length) {
      $showMessage = { error: "Please fill all entries first" };
      return;
    }

    if (!documentPath.length) {
      $showMessage = { error: "Please fill all entries first" };
      return;
    }

    value = uuidv4();
  };

  const handleDownload = () => {
    let imgElement = qrCodeElement.querySelector("img.qrcode");
    let base64Image = imgElement.src;

    const downloadLink = document.createElement("a");
    downloadLink.href = base64Image;
    downloadLink.download = "Image.png";
    downloadLink.click();
  };

  let routeName = "";
  let documentPath = "";
  let documentName = "";
  let documentDescription = "";

  const handleInput = (event: Event) => {
    const target = event.target as HTMLInputElement;
    documentName = target.value;
  };

  const handleTextArea = (event: Event) => {
    const target = event.target as HTMLInputElement;
    documentDescription = target.value;
  };

  let routes = [
    { id: 1, name: "Love", route: "I / Love / You" },
    { id: 2, name: "Hate", route: "I / Hate / You" },
  ];

  const handleRouteExpand = () => {
    $routeExpand = !$routeExpand;
  };

  const registrationMethod = "POST";
  const registrationAddress = `${address}/document_register`;
  const registrationRequest: RequestAPI = {
    method: registrationMethod,
    address: registrationAddress,
    credentials: {
      codeData: "",
      documentName: "",
      documentDescription: "",
    },
  };

  const handleSubmit = async () => {
    registrationRequest.credentials!.codeData = value;
    registrationRequest.credentials!.documentName = documentName;
    registrationRequest.credentials!.documentDescription = documentDescription;

    const request: ResponseData = await handleFetch(
      registrationRequest,
      authToken
    );

    if (request.error) {
      $showMessage = request;
    }
  };
</script>

<div class="register-document-wrapper">
  <form class="register-document-form" on:submit|preventDefault={handleSubmit}>
    <div class="credential-wrapper">
      <span class="date" class:dark={$dark}
        >Author: {fullname.firstName}
        {fullname.middleName}
        {fullname.lastName}</span
      >
      <Input
        inputName="Document Name"
        inputType="Text"
        overlap={true}
        on:input={handleInput}
        dark={$dark}
      ></Input>
      <!-- svelte-ignore a11y-click-events-have-key-events -->
      <!-- svelte-ignore a11y-no-static-element-interactions -->
      <div
        class="route-options-wrapper"
        on:click|stopPropagation={handleRouteExpand}
      >
        {#if routeName.length}
          {#each routes as route (route.id)}
            {#if routeName === route.name}
              <span class="route-name"> {route.name}: {route.route} </span>
            {/if}
          {/each}
        {:else}
          <span class="route-name"> Select a Route </span>
        {/if}
        <TriangleIcon rotate={$routeExpand}></TriangleIcon>
      </div>
      <div
        class="route-options-wrapper-expand"
        class:wrapper-expand={$routeExpand}
      >
        <ul class="route-wrapper">
          {#each routes as route (route.id)}
            <!-- svelte-ignore a11y-click-events-have-key-events -->
            <!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
            <!-- svelte-ignore missing-declaration -->
            <li
              on:click={() => {
                routeName = route.name;
                documentPath = route.route;
                $routeExpand = false;
              }}
            >
              <span
                class="route-name"
                class:active={route.name === routeName && true}
                >{route.name}: {route.route}
              </span>
            </li>
          {/each}
        </ul>
      </div>
      <textarea placeholder="Description" on:input={handleTextArea} required
      ></textarea>
      <div class="button-wrapper">
        <div class="button">
          <Button>Submit</Button>
        </div>
      </div>
    </div>
    <div class="code-wrapper">
      <span class="date" class:dark={$dark}>{date}</span>
      <!-- svelte-ignore missing-declaration -->
      <!-- svelte-ignore a11y-click-events-have-key-events -->
      <!-- svelte-ignore a11y-no-static-element-interactions -->
      <div
        class="code-placeholder"
        bind:this={qrCodeElement}
        on:click|stopPropagation={handleGenerate}
        on:mouseenter={() => {
          placeholderHovered = true;
        }}
        on:mouseleave={() => {
          placeholderHovered = false;
        }}
      >
        {#if value && value.length}
          <QrCode {value}></QrCode>
          {#if value && value.length && placeholderHovered}
            <div transition:fade class="code-overlap" on:click={handleDownload}>
              <span class="download-qr">Download Image</span>
            </div>
          {/if}
        {:else}
          <span class="qr-label">Generate QR Code</span>
        {/if}
      </div>
    </div>
  </form>
</div>

<style>
  span {
    font-size: 1rem;
    font-weight: 700;
    color: var(--scroll-color);
    transition: all ease-in-out 300ms;
  }

  span.dark {
    color: var(--background);
  }

  div.register-document-wrapper {
    padding: 2rem;
    height: 100%;

    & form {
      display: flex;
      justify-content: center;
      column-gap: 10rem;
      height: 100%;

      & div.credential-wrapper {
        width: 100%;
        position: relative;

        & div.route-options-wrapper {
          transition: all ease-in-out 300ms;
          width: 100%;
          border: 1px solid var(--header-color);
          margin-bottom: 1rem;
          padding: 0.5rem;
          border-radius: 0.5rem;
          display: flex;
          align-items: center;
          justify-content: space-between;
          cursor: pointer;

          & span.route-name {
            font-weight: normal;
            font-size: 0.9rem;
          }
        }

        & div.route-options-wrapper-expand {
          display: grid;
          grid-template-rows: 0fr;
          border-radius: 0.5rem;
          position: absolute;
          top: 8.5rem;
          z-index: 1;
          overflow: hidden;
          transition: all ease-in-out 400ms;
          background-color: var(--background);
          box-shadow: 2px 3px 5px rgba(0, 0, 0, 0.3);

          width: 100%;

          & ul.route-wrapper {
            min-height: 0;

            & li {
              display: flex;
              align-items: center;
              column-gap: 0.5rem;
              margin: 0.2rem;
              padding: 0.3rem 0.5rem;
              border-radius: 0.4rem;
              transition: all ease-in-out 500ms;
              cursor: pointer;

              & span.route-name {
                font-weight: normal;
                font-size: 0.9rem;
              }
            }

            & li:hover {
              background-color: var(--main-col-2);
            }
          }
        }

        & div.route-options-wrapper-expand.wrapper-expand {
          grid-template-rows: 1fr;
        }

        & div.route-options-wrapper:hover {
          background-color: var(--header-color);
        }

        & textarea {
          outline: none;
          transition: 300ms;
          background-color: transparent;
          border-radius: 0.5rem;
          padding: 0.5rem;
          width: 100%;
          height: 70%;
          min-width: 20%;
          min-height: 20%;
          border: 1px solid var(--header-color);
          color: var(--scroll-color);
        }

        & textarea:hover {
          border-color: var(--border-hover-color);
        }

        & textarea:focus {
          border-color: var(--border-active-color);
        }

        & div.button-wrapper {
          text-align: end;

          & div.button {
            display: inline-block;
            width: 10rem;
            margin-top: 1rem;
          }
        }
      }

      & div.code-wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-between;

        & div.code-placeholder {
          overflow: hidden;
          position: relative;
          border-radius: 1rem;
          transition: all ease-in-out 300ms;
          background-color: var(--main-col-1);
          width: 15rem;
          height: 15rem;
          display: flex;
          align-items: center;
          justify-content: center;
          cursor: pointer;

          & span.qr-label {
            transition: color ease-in-out 300ms;
            color: var(--background);
            margin: auto;
            font-weight: normal;
            font-size: 0.9rem;
          }

          & img.qrcode {
            border-radius: 0.5rem;
          }

          & div.code-overlap {
            position: absolute;
            transition: all ease-in-out 300ms;
            inset: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 1;

            & span.download-qr {
              color: var(--background);
            }
          }

          & div.code-overlap:hover {
            background-color: rgba(84, 84, 84, 0.9);
          }
        }

        & div.code-placeholder:hover {
          background-color: var(--main-col-2);
          box-shadow: 1px 2px 3px var(--main-col-2);
        }

        & div.code-placeholder:hover span.qr-label {
          color: var(--scroll-color);
        }
      }
    }
  }
</style>
