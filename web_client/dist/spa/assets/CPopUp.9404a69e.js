import{j as v,w as V,ay as xe,s as Se,x as H,n as R,az as I,k as ne,r as P,I as qe,M as Be,l as y,aA as Ce,aB as Pe,aC as Te,P as ae,u as M,aD as le,a3 as Fe,W as ie,i as _e,aE as Ee,aF as X,aG as $e,U as Y,p as De,a8 as Ve,af as He,au as Me,ag as ze,ah as Ae,ak as Oe,am as Qe,ar as Ue,aj as je,aH as L,aI as Ie}from"./index.14fb0c53.js";const mt={dark:{type:Boolean,default:null}};function vt(e,t){return v(()=>e.dark===null?t.dark.isActive:e.dark)}let b=[],T=[];function se(e){T=T.filter(t=>t!==e)}function Le(e){se(e),T.push(e)}function Z(e){se(e),T.length===0&&b.length!==0&&(b[b.length-1](),b=[])}function Ke(e){T.length===0?e():b.push(e)}function ht(e){b=b.filter(t=>t!==e)}const Re={modelValue:{type:Boolean,default:null},"onUpdate:modelValue":[Function,Array]},Ge=["beforeShow","show","beforeHide","hide"];function Ne({showing:e,canShow:t,hideOnRouteChange:o,handleShow:l,handleHide:i,processOnMount:d}){const u=H(),{props:s,emit:r,proxy:m}=u;let f;function h(a){e.value===!0?x(a):g(a)}function g(a){if(s.disable===!0||a!==void 0&&a.qAnchorHandled===!0||t!==void 0&&t(a)!==!0)return;const p=s["onUpdate:modelValue"]!==void 0;p===!0&&(r("update:modelValue",!0),f=a,R(()=>{f===a&&(f=void 0)})),(s.modelValue===null||p===!1)&&q(a)}function q(a){e.value!==!0&&(e.value=!0,r("beforeShow",a),l!==void 0?l(a):r("show",a))}function x(a){if(s.disable===!0)return;const p=s["onUpdate:modelValue"]!==void 0;p===!0&&(r("update:modelValue",!1),f=a,R(()=>{f===a&&(f=void 0)})),(s.modelValue===null||p===!1)&&F(a)}function F(a){e.value!==!1&&(e.value=!1,r("beforeHide",a),i!==void 0?i(a):r("hide",a))}function B(a){s.disable===!0&&a===!0?s["onUpdate:modelValue"]!==void 0&&r("update:modelValue",!1):a===!0!==e.value&&(a===!0?q:F)(f)}V(()=>s.modelValue,B),o!==void 0&&xe(u)===!0&&V(()=>m.$route.fullPath,()=>{o.value===!0&&e.value===!0&&x()}),d===!0&&Se(()=>{B(s.modelValue)});const _={show:g,hide:x,toggle:h};return Object.assign(m,_),_}const K=[];function gt(e,t){do{if(e.$options.name==="QMenu"){if(e.hide(t),e.$props.separateClosePopup===!0)return I(e)}else if(e.__qPortal===!0){const o=I(e);return o!==void 0&&o.$options.name==="QPopupProxy"?(e.hide(t),o):e}e=I(e)}while(e!=null)}const We=ne({name:"QPortal",setup(e,{slots:t}){return()=>t.default()}});function Je(e){for(e=e.parent;e!=null;){if(e.type.name==="QGlobalDialog")return!0;if(e.type.name==="QDialog"||e.type.name==="QMenu")return!1;e=e.parent}return!1}function Xe(e,t,o,l){const i=P(!1),d=P(!1);let u=null;const s={},r=l==="dialog"&&Je(e);function m(h){if(h===!0){Z(s),d.value=!0;return}d.value=!1,i.value===!1&&(r===!1&&u===null&&(u=Pe(!1,l)),i.value=!0,K.push(e.proxy),Le(s))}function f(h){if(d.value=!1,h!==!0)return;Z(s),i.value=!1;const g=K.indexOf(e.proxy);g!==-1&&K.splice(g,1),u!==null&&(Te(u),u=null)}return qe(()=>{f(!0)}),e.proxy.__qPortal=!0,Be(e.proxy,"contentEl",()=>t.value),{showPortal:m,hidePortal:f,portalIsActive:i,portalIsAccessible:d,renderPortal:()=>r===!0?o():i.value===!0?[y(Ce,{to:u},y(We,o))]:void 0}}const Ye={transitionShow:{type:String,default:"fade"},transitionHide:{type:String,default:"fade"},transitionDuration:{type:[String,Number],default:300}};function Ze(e,t=()=>{},o=()=>{}){return{transitionProps:v(()=>{const l=`q-transition--${e.transitionShow||t()}`,i=`q-transition--${e.transitionHide||o()}`;return{appear:!0,enterFromClass:`${l}-enter-from`,enterActiveClass:`${l}-enter-active`,enterToClass:`${l}-enter-to`,leaveFromClass:`${i}-leave-from`,leaveActiveClass:`${i}-leave-active`,leaveToClass:`${i}-leave-to`}}),transitionStyle:v(()=>`--q-transition-duration: ${e.transitionDuration}ms`)}}function et(){let e;const t=H();function o(){e=void 0}return ae(o),M(o),{removeTick:o,registerTick(l){e=l,R(()=>{e===l&&(le(t)===!1&&e(),e=void 0)})}}}function tt(){let e=null;const t=H();function o(){e!==null&&(clearTimeout(e),e=null)}return ae(o),M(o),{removeTimeout:o,registerTimeout(l,i){o(),le(t)===!1&&(e=setTimeout(()=>{e=null,l()},i))}}}const k=[];let S;function ot(e){S=e.keyCode===27}function nt(){S===!0&&(S=!1)}function at(e){S===!0&&(S=!1,Fe(e,27)===!0&&k[k.length-1](e))}function ue(e){window[e]("keydown",ot),window[e]("blur",nt),window[e]("keyup",at),S=!1}function lt(e){ie.is.desktop===!0&&(k.push(e),k.length===1&&ue("addEventListener"))}function ee(e){const t=k.indexOf(e);t!==-1&&(k.splice(t,1),k.length===0&&ue("removeEventListener"))}const w=[];function re(e){w[w.length-1](e)}function it(e){ie.is.desktop===!0&&(w.push(e),w.length===1&&document.body.addEventListener("focusin",re))}function te(e){const t=w.indexOf(e);t!==-1&&(w.splice(t,1),w.length===0&&document.body.removeEventListener("focusin",re))}function pt(){return _e(Ee)}function st(e,t,o){let l;function i(){l!==void 0&&(X.remove(l),l=void 0)}return M(()=>{e.value===!0&&i()}),{removeFromHistory:i,addToHistory(){l={condition:()=>o.value===!0,handler:t},X.add(l)}}}function ut(){let e;return{preventBodyScroll(t){t!==e&&(e!==void 0||t===!0)&&(e=t,$e(t))}}}let D=0;const rt={standard:"fixed-full flex-center",top:"fixed-top justify-center",bottom:"fixed-bottom justify-center",right:"fixed-right items-center",left:"fixed-left items-center"},oe={standard:["scale","scale"],top:["slide-down","slide-up"],bottom:["slide-up","slide-down"],right:["slide-left","slide-right"],left:["slide-right","slide-left"]};var dt=ne({name:"QDialog",inheritAttrs:!1,props:{...Re,...Ye,transitionShow:String,transitionHide:String,persistent:Boolean,autoClose:Boolean,allowFocusOutside:Boolean,noEscDismiss:Boolean,noBackdropDismiss:Boolean,noRouteDismiss:Boolean,noRefocus:Boolean,noFocus:Boolean,noShake:Boolean,seamless:Boolean,maximized:Boolean,fullWidth:Boolean,fullHeight:Boolean,square:Boolean,backdropFilter:String,position:{type:String,default:"standard",validator:e=>e==="standard"||["top","bottom","left","right"].includes(e)}},emits:[...Ge,"shake","click","escapeKey"],setup(e,{slots:t,emit:o,attrs:l}){const i=H(),d=P(null),u=P(!1),s=P(!1);let r=null,m=null,f,h;const g=v(()=>e.persistent!==!0&&e.noRouteDismiss!==!0&&e.seamless!==!0),{preventBodyScroll:q}=ut(),{registerTimeout:x}=tt(),{registerTick:F,removeTick:B}=et(),{transitionProps:_,transitionStyle:a}=Ze(e,()=>oe[e.position][0],()=>oe[e.position][1]),p=v(()=>a.value+(e.backdropFilter!==void 0?`;backdrop-filter:${e.backdropFilter};-webkit-backdrop-filter:${e.backdropFilter}`:"")),{showPortal:G,hidePortal:N,portalIsAccessible:de,renderPortal:ce}=Xe(i,d,we,"dialog"),{hide:E}=Ne({showing:u,hideOnRouteChange:g,handleShow:pe,handleHide:ye,processOnMount:!0}),{addToHistory:fe,removeFromHistory:me}=st(u,E,g),ve=v(()=>`q-dialog__inner flex no-pointer-events q-dialog__inner--${e.maximized===!0?"maximized":"minimized"} q-dialog__inner--${e.position} ${rt[e.position]}`+(s.value===!0?" q-dialog__inner--animating":"")+(e.fullWidth===!0?" q-dialog__inner--fullwidth":"")+(e.fullHeight===!0?" q-dialog__inner--fullheight":"")+(e.square===!0?" q-dialog__inner--square":"")),$=v(()=>u.value===!0&&e.seamless!==!0),he=v(()=>e.autoClose===!0?{onClick:be}:{}),ge=v(()=>[`q-dialog fullscreen no-pointer-events q-dialog--${$.value===!0?"modal":"seamless"}`,l.class]);V(()=>e.maximized,n=>{u.value===!0&&O(n)}),V($,n=>{q(n),n===!0?(it(Q),lt(A)):(te(Q),ee(A))});function pe(n){fe(),m=e.noRefocus===!1&&document.activeElement!==null?document.activeElement:null,O(e.maximized),G(),s.value=!0,e.noFocus!==!0?(document.activeElement!==null&&document.activeElement.blur(),F(C)):B(),x(()=>{if(i.proxy.$q.platform.is.ios===!0){if(e.seamless!==!0&&document.activeElement){const{top:c,bottom:U}=document.activeElement.getBoundingClientRect(),{innerHeight:J}=window,j=window.visualViewport!==void 0?window.visualViewport.height:J;c>0&&U>j/2&&(document.scrollingElement.scrollTop=Math.min(document.scrollingElement.scrollHeight-j,U>=J?1/0:Math.ceil(document.scrollingElement.scrollTop+U-j/2))),document.activeElement.scrollIntoView()}h=!0,d.value.click(),h=!1}G(!0),s.value=!1,o("show",n)},e.transitionDuration)}function ye(n){B(),me(),W(!0),s.value=!0,N(),m!==null&&(((n&&n.type.indexOf("key")===0?m.closest('[tabindex]:not([tabindex^="-"])'):void 0)||m).focus(),m=null),x(()=>{N(!0),s.value=!1,o("hide",n)},e.transitionDuration)}function C(n){Ke(()=>{let c=d.value;c===null||c.contains(document.activeElement)===!0||(c=(n!==""?c.querySelector(n):null)||c.querySelector("[autofocus][tabindex], [data-autofocus][tabindex]")||c.querySelector("[autofocus] [tabindex], [data-autofocus] [tabindex]")||c.querySelector("[autofocus], [data-autofocus]")||c,c.focus({preventScroll:!0}))})}function z(n){n&&typeof n.focus=="function"?n.focus({preventScroll:!0}):C(),o("shake");const c=d.value;c!==null&&(c.classList.remove("q-animate--scale"),c.classList.add("q-animate--scale"),r!==null&&clearTimeout(r),r=setTimeout(()=>{r=null,d.value!==null&&(c.classList.remove("q-animate--scale"),C())},170))}function A(){e.seamless!==!0&&(e.persistent===!0||e.noEscDismiss===!0?e.maximized!==!0&&e.noShake!==!0&&z():(o("escapeKey"),E()))}function W(n){r!==null&&(clearTimeout(r),r=null),(n===!0||u.value===!0)&&(O(!1),e.seamless!==!0&&(q(!1),te(Q),ee(A))),n!==!0&&(m=null)}function O(n){n===!0?f!==!0&&(D<1&&document.body.classList.add("q-body--dialog"),D++,f=!0):f===!0&&(D<2&&document.body.classList.remove("q-body--dialog"),D--,f=!1)}function be(n){h!==!0&&(E(n),o("click",n))}function ke(n){e.persistent!==!0&&e.noBackdropDismiss!==!0?E(n):e.noShake!==!0&&z()}function Q(n){e.allowFocusOutside!==!0&&de.value===!0&&Ve(d.value,n.target)!==!0&&C('[tabindex]:not([tabindex="-1"])')}Object.assign(i.proxy,{focus:C,shake:z,__updateRefocusTarget(n){m=n||null}}),M(W);function we(){return y("div",{role:"dialog","aria-modal":$.value===!0?"true":"false",...l,class:ge.value},[y(Y,{name:"q-transition--fade",appear:!0},()=>$.value===!0?y("div",{class:"q-dialog__backdrop fixed-full",style:p.value,"aria-hidden":"true",tabindex:-1,onClick:ke}):null),y(Y,_.value,()=>u.value===!0?y("div",{ref:d,class:ve.value,style:a.value,tabindex:-1,...he.value},De(t.default)):null)])}return ce}});const ct=He({__name:"CPopUp",props:Me({value:{type:Boolean,default:!1},seamless:{type:Boolean,default:!1},position:{type:String,default:"right"},width:{type:Number},persistent:{type:Boolean,default:!1}},{modelValue:{type:Boolean},modelModifiers:{}}),emits:["update:modelValue"],setup(e){const t=e,o=ze(e,"modelValue"),l=v(()=>({width:`${t.width}px`}));return(i,d)=>(Ae(),Oe(dt,{seamless:e.seamless,position:e.position,persistent:e.persistent,value:e.value,modelValue:o.value,"onUpdate:modelValue":d[0]||(d[0]=u=>o.value=u)},{default:Qe(()=>[je("div",{class:"popup",style:Ie([{"max-width":"2000px"},l.value])},[L(i.$slots,"header",{},void 0,!0),L(i.$slots,"default",{},void 0,!0),L(i.$slots,"footer",{},void 0,!0)],4)]),_:3},8,["seamless","position","persistent","value","modelValue"]))}});var yt=Ue(ct,[["__scopeId","data-v-7602e617"]]);export{yt as C,dt as Q,Ke as a,vt as b,Re as c,Ye as d,Ge as e,et as f,tt as g,Ze as h,Ne as i,Xe as j,it as k,te as l,ee as m,gt as n,lt as o,K as p,pt as q,ht as r,mt as u};
