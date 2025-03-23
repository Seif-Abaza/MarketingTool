import asyncio
import datetime
import json
import logging
import os
import random
import re
import sys
import time
import traceback
from io import StringIO
from random import randrange
from time import sleep

import pyperclip

# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright
from PySide6.QtWidgets import QDialog, QListView, QMessageBox

from utils.helper import helper

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
FB_SCRIPT = """ console.clear();var ee=Object.defineProperty,te=(e,t,n)=>t in e?ee(e,t,{enumerable:!0,configurable:!0,writable:!0,value:n}):e[t]=n,P=(e,t,n)=>te(e,"symbol"!=typeof t?t+"":t,n);let S=(t,e)=>e.some(e=>t instanceof e),M,H;function ne(){return M=M||[IDBDatabase,IDBObjectStore,IDBIndex,IDBCursor,IDBTransaction]}function ie(){return H=H||[IDBCursor.prototype.advance,IDBCursor.prototype.continue,IDBCursor.prototype.continuePrimaryKey]}let C=new WeakMap,E=new WeakMap,_=new WeakMap;function oe(o){var e=new Promise((e,t)=>{let n=()=>{o.removeEventListener("success",i),o.removeEventListener("error",r)},i=()=>{e(h(o.result)),n()},r=()=>{t(o.error),n()};o.addEventListener("success",i),o.addEventListener("error",r)});return _.set(e,o),e}function re(o){var e;C.has(o)||(e=new Promise((e,t)=>{let n=()=>{o.removeEventListener("complete",i),o.removeEventListener("error",r),o.removeEventListener("abort",r)},i=()=>{e(),n()},r=()=>{t(o.error||new DOMException("AbortError","AbortError")),n()};o.addEventListener("complete",i),o.addEventListener("error",r),o.addEventListener("abort",r)}),C.set(o,e))}let O={get(e,t,n){if(e instanceof IDBTransaction){if("done"===t)return C.get(e);if("store"===t)return n.objectStoreNames[1]?void 0:n.objectStore(n.objectStoreNames[0])}return h(e[t])},set(e,t,n){return e[t]=n,!0},has(e,t){return e instanceof IDBTransaction&&("done"===t||"store"===t)||t in e}};function U(e){O=e(O)}function se(t){return ie().includes(t)?function(...e){return t.apply(j(this),e),h(this.request)}:function(...e){return h(t.apply(j(this),e))}}function ae(e){return"function"==typeof e?se(e):(e instanceof IDBTransaction&&re(e),S(e,ne())?new Proxy(e,O):e)}function h(e){var t;return e instanceof IDBRequest?oe(e):E.has(e)?E.get(e):((t=ae(e))!==e&&(E.set(e,t),_.set(t,e)),t)}let j=e=>_.get(e);function ce(e,t,{blocked:n,upgrade:i,blocking:r,terminated:o}={}){let s=indexedDB.open(e,t),a=h(s);return i&&s.addEventListener("upgradeneeded",e=>{i(h(s.result),e.oldVersion,e.newVersion,h(s.transaction),e)}),n&&s.addEventListener("blocked",e=>n(e.oldVersion,e.newVersion,e)),a.then(e=>{o&&e.addEventListener("close",()=>o()),r&&e.addEventListener("versionchange",e=>r(e.oldVersion,e.newVersion,e))}).catch(()=>{}),a}let de=["get","getKey","getAll","getAllKeys","count"],le=["put","add","delete","clear"],D=new Map;function R(e,t){if(e instanceof IDBDatabase&&!(t in e)&&"string"==typeof t){if(D.get(t))return D.get(t);let i=t.replace(/FromIndex$/,""),r=t!==i,o=le.includes(i);return i in(r?IDBIndex:IDBObjectStore).prototype&&(o||de.includes(i))?(e=async function(e,...t){e=this.transaction(e,o?"readwrite":"readonly");let n=e.store;return r&&(n=n.index(t.shift())),(await Promise.all([n[i](...t),o&&e.done]))[0]},D.set(t,e),e):void 0}}U(i=>({...i,get:(e,t,n)=>R(e,t)||i.get(e,t,n),has:(e,t)=>!!R(e,t)||i.has(e,t)}));let ue=["continue","continuePrimaryKey","advance"],V={},k=new WeakMap,N=new WeakMap,fe={get(e,t){if(!ue.includes(t))return e[t];let n=V[t];return n=n||(V[t]=function(...e){k.set(this,N.get(this)[t](...e))})}};async function*pe(...e){let t=this;if(t=t instanceof IDBCursor?t:await t.openCursor(...e)){t=t;var n=new Proxy(t,fe);for(N.set(n,t),_.set(n,j(t));t;)yield n,t=await(k.get(n)||t.continue()),k.delete(n)}}function F(e,t){return t===Symbol.asyncIterator&&S(e,[IDBIndex,IDBObjectStore,IDBCursor])||"iterate"===t&&S(e,[IDBIndex,IDBObjectStore])}U(i=>({...i,get(e,t,n){return F(e,t)?pe:i.get(e,t,n)},has(e,t){return F(e,t)||i.has(e,t)}}));var J,f=function(e,s,a,d){return new(a=a||Promise)(function(n,t){function i(e){try{o(d.next(e))}catch(e){t(e)}}function r(e){try{o(d.throw(e))}catch(e){t(e)}}function o(e){var t;e.done?n(e.value):((t=e.value)instanceof a?t:new a(function(e){e(t)})).then(i,r)}o((d=d.apply(e,s||[])).next())})},he=function(e,t){var n={};for(r in e)Object.prototype.hasOwnProperty.call(e,r)&&t.indexOf(r)<0&&(n[r]=e[r]);if(null!=e&&"function"==typeof Object.getOwnPropertySymbols)for(var i=0,r=Object.getOwnPropertySymbols(e);i<r.length;i++)t.indexOf(r[i])<0&&Object.prototype.propertyIsEnumerable.call(e,r[i])&&(n[r[i]]=e[r[i]]);return n};class ge{constructor(e){this.name="scrape-storage",this.persistent=!0,this.data=new Map,null!=e&&e.name&&(this.name=e.name),null!=e&&e.persistent&&(this.persistent=e.persistent),this.initDB().then(()=>{}).catch(()=>{this.persistent=!1})}get storageKey(){return"storage-"+this.name}initDB(){return f(this,void 0,void 0,function*(){this.db=yield ce(this.storageKey,6,{upgrade(e,t,n,i){let r;if(t<5)try{e.deleteObjectStore("data")}catch{}(r=e.objectStoreNames.contains("data")?i.objectStore("data"):e.createObjectStore("data",{keyPath:"_id",autoIncrement:!0}))&&!r.indexNames.contains("_createdAt")&&r.createIndex("_createdAt","_createdAt"),r&&!r.indexNames.contains("_groupId")&&r.createIndex("_groupId","_groupId"),r&&!r.indexNames.contains("_pk")&&r.createIndex("_pk","_pk",{unique:!0})}})})}_dbGetElem(e,t){return f(this,void 0,void 0,function*(){if(this.persistent&&this.db)return yield(t=t||this.db.transaction("data","readonly")).store.index("_pk").get(e);throw new Error("DB doesnt exist")})}getElem(e){return f(this,void 0,void 0,function*(){if(this.persistent&&this.db)try{return yield this._dbGetElem(e)}catch(e){console.error(e)}else this.data.get(e)})}_dbSetElem(i,r,o=!1,s,a){return f(this,void 0,void 0,function*(){if(this.persistent&&this.db){let e=!1;var t=(a=a||this.db.transaction("data","readwrite")).store,n=yield t.index("_pk").get(i);return n?o&&(yield t.put(Object.assign(Object.assign({},n),r)),e=!0):(n=Object.assign({_pk:i,_createdAt:new Date},r),s&&(n._groupId=s),yield t.put(n),e=!0),e}throw new Error("DB doesnt exist")})}addElem(e,t,n=!1,i){return f(this,void 0,void 0,function*(){if(this.persistent&&this.db)try{return yield this._dbSetElem(e,t,n,i)}catch(e){console.error(e)}else this.data.set(e,t);return!0})}addElems(t,o=!1,s){return f(this,void 0,void 0,function*(){if(this.persistent&&this.db){let n=[],i=this.db.transaction("data","readwrite"),r=[];if(t.forEach(([e,t])=>{-1===r.indexOf(e)&&(r.push(e),n.push(this._dbSetElem(e,t,o,s,i)))}),0<n.length){n.push(i.done);var e=yield Promise.all(n);let t=0;return e.forEach(e=>{"boolean"==typeof e&&e&&(t+=1)}),t}return 0}return t.forEach(([e,t])=>{this.addElem(e,t)}),t.length})}deleteFromGroupId(n){return f(this,void 0,void 0,function*(){if(this.persistent&&this.db){let e=0,t=yield this.db.transaction("data","readwrite").store.index("_groupId").openCursor(IDBKeyRange.only(n));for(;t;)t.delete(),t=yield t.continue(),e+=1;return e}throw new Error("Not Implemented Error")})}clear(){return f(this,void 0,void 0,function*(){this.persistent&&this.db?yield this.db.clear("data"):this.data.clear()})}getCount(){return f(this,void 0,void 0,function*(){return this.persistent&&this.db?yield this.db.count("data"):this.data.size})}getAll(){return f(this,void 0,void 0,function*(){if(this.persistent&&this.db){let n=new Map,e=yield this.db.getAll("data");return e&&e.forEach(e=>{var t=e._id,e=he(e,["_id"]);n.set(t,e)}),n}return this.data})}toCsvData(){return f(this,void 0,void 0,function*(){let t=[];return t.push(this.headers),(yield this.getAll()).forEach(e=>{try{t.push(this.itemToRow(e))}catch(e){console.error(e)}}),t})}}let ye=["display: block;","padding: 0px 4px;","cursor: pointer;","text-align: center;"];function W(e){var t=document.createElement("div"),n=[...ye];return t.setAttribute("style",n.join("")),t}let we=["margin-left: 4px;","margin-right: 4px;","border-left: 1px solid #2e2e2e;"];function X(){var e=document.createElement("div");return e.innerHTML="&nbsp;",e.setAttribute("style",we.join("")),e}function w(e,t){t=t||{};let n;var i,r=document.createElement("span");return(n=t.bold?(i=document.createElement("strong"),r.append(i),i):r).textContent=e,t.idAttribute&&n.setAttribute("id",t.idAttribute),r}let me=["position: fixed;","top: 0;","left: 0;","z-index: 10000;","width: 100%;","height: 100%;","pointer-events: none;"],be=["position: absolute;","bottom: 30px;","right: 30px;","width: auto;","pointer-events: auto;"],_e=["align-items: center;","appearance: none;","background-color: #EEE;","border-radius: 4px;","border-width: 0;","box-shadow: rgba(45, 35, 66, 0.4) 0 2px 4px,rgba(45, 35, 66, 0.3) 0 7px 13px -3px,#D6D6E7 0 -3px 0 inset;","box-sizing: border-box;","color: #36395A;","display: flex;","font-family: monospace;","height: 38px;","justify-content: space-between;","line-height: 1;","list-style: none;","overflow: hidden;","padding-left: 16px;","padding-right: 16px;","position: relative;","text-align: left;","text-decoration: none;","user-select: none;","white-space: nowrap;","font-size: 18px;"];class xe{constructor(){this.ctas=[],this.canva=document.createElement("div"),this.canva.setAttribute("style",me.join("")),this.inner=document.createElement("div"),this.inner.setAttribute("style",be.join("")),this.canva.appendChild(this.inner),this.history=document.createElement("div"),this.inner.appendChild(this.history),this.container=document.createElement("div"),this.container.setAttribute("style",_e.join("")),this.inner.appendChild(this.container)}makeItDraggable(){let t=0,n=0,i=0,r=0,o=e=>{i=e.clientX-t,r=e.clientY-n,this.inner.style.right=window.innerWidth-i-this.inner.offsetWidth+"px",this.inner.style.bottom=window.innerHeight-r-this.inner.offsetHeight+"px"};this.inner.addEventListener("mousedown",e=>{e.preventDefault(),t=e.clientX-this.inner.offsetLeft,n=e.clientY-this.inner.offsetTop,window.addEventListener("mousemove",o,!1)},!1),window.addEventListener("mouseup",()=>{window.removeEventListener("mousemove",o,!1)},!1);var e=document.createElement("div");e.style.cursor="move",e.innerHTML='<svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height="18px" width="18px" xmlns="http://www.w3.org/2000/svg"><polyline points="5 9 2 12 5 15"></polyline><polyline points="9 5 12 2 15 5"></polyline><polyline points="15 19 12 22 9 19"></polyline><polyline points="19 9 22 12 19 15"></polyline><line x1="2" y1="12" x2="22" y2="12"></line><line x1="12" y1="2" x2="12" y2="22"></line></svg>',this.addCta(X()),this.addCta(e)}render(){document.body.appendChild(this.canva)}addCta(e,t){"u"<typeof t?this.ctas.push(e):this.ctas.splice(t,0,e),this.container.innerHTML="",this.ctas.forEach(e=>{this.container.appendChild(e)})}}(e=>{e.ADD="add",e.LOG="log"})(J=J||{});class Ie extends ge{constructor(){super(...arguments),P(this,"name","fb-storage")}get headers(){return["Profile Id","Full Name","Profile Link","Bio","ImageSrc","GroupId","Group Joining Text","Profile Type"]}itemToRow(e){return[e.profileId,e.fullName,e.profileLink,e.bio,e.imageSrc,e.groupId,e.groupJoiningText,e.profileType]}}let y=[],g=!1,K=[],m=new xe,plx=new Ie,Y="fbnumber-tracker";async function b(){if(g){for(var[e,t]of K=await plx.getAll()){e={Id:e,profileId:t.profileId,name:t.fullName,bio:t.bio,url:t.profileLink,image:t.imageSrc,group_id:t.groupId,group_joining_text:t.groupJoiningText,profile_type:t.profileType,created_at:(new Date).toISOString(),updated_at:(new Date).toISOString(),source:"facebook"};y.push(e)}return plx.clear()}var n,i=document.getElementById(Y);i&&(n=await plx.getCount(),i.textContent=n.toString()),setTimeout(()=>{window.scrollTo({top:document.body.scrollHeight-10,left:0,behavior:"smooth"})},9e3)}function ve(){var e=W(),e=(e.appendChild(w("Click if you want finished , Get ")),e.appendChild(w("0",{bold:!0,idAttribute:Y})),e.appendChild(w(" users")),e.addEventListener("click",async function(){g?await plx.clear():g=!0,await b()}),m.addCta(e),m.addCta(X()),W());e.appendChild(w("Reset")),e.addEventListener("click",async function(){g&&(await plx.clear(),await b())}),m.addCta(e),m.render()}function Ee(e){let t,n,i,r,o,s,a;if(null!=(t=null==e?void 0:e.data)&&t.group)a=e.data.group;else{if("Group"!==(null==(i=null==(n=null==e?void 0:e.data)?void 0:n.node)?void 0:i.__typename))return;a=e.data.node}let d;if(null!=(r=null==a?void 0:a.new_members)&&r.edges)d=a.new_members.edges;else if(null!=(o=null==a?void 0:a.new_forum_members)&&o.edges)d=a.new_forum_members.edges;else{if(null==(s=null==a?void 0:a.search_results)||!s.edges)return;d=a.search_results.edges}let l=d.map(e=>{var t,n,i,r,o,s,a,d="GroupUserInvite"===e.node.__isEntity?e.node.invitee_profile:e.node;return d?({id:t,name:n,bio_text:i,url:r,profile_picture:o,__isProfile:s}=d,a=(null==(a=null==e?void 0:e.join_status_text)?void 0:a.text)||(null==(e=null==(a=null==e?void 0:e.membership)?void 0:a.join_status_text)?void 0:e.text),d=null==(e=d.group_membership)?void 0:e.associated_group.id,{profileId:t,fullName:n,profileLink:r,bio:(null==i?void 0:i.text)||"",imageSrc:(null==o?void 0:o.uri)||"",groupId:d,groupJoiningText:a||"",profileType:s}):null}),u=[];l.forEach(e=>{e&&u.push([e.profileId,e])}),plx.addElems(u).then(()=>{b()})}function De(e){var n=[];try{n.push(JSON.parse(e))}catch(t){var i=e.split(`
`);if(i.length<=1)return void console.error("Fail to parse API response",t);for(let e=0;e<i.length;e++){var r=i[e];try{n.push(JSON.parse(r))}catch{console.error("Fail to parse API response",t)}}}for(let e=0;e<n.length;e++)Ee(n[e])}function Se(){ve(),window.scrollTo({top:document.body.scrollHeight-10,left:0,behavior:"smooth"});let e=XMLHttpRequest.prototype.open;return XMLHttpRequest.prototype.open=function(){this.addEventListener("readystatechange",function(){if(this.responseURL.includes("/api/graphql/")&&4===this.readyState){if(g)return y.forEach(e=>{console.log(JSON.stringify({Id:e.Id,profileId:e.profileId,name:e.name,bio:e.bio,url:e.url,image:e.image,group_id:e.group_id,group_joining_text:e.group_joining_text,profile_type:e.profile_type,created_at:(new Date).toISOString(),updated_at:(new Date).toISOString(),source:"facebook"}))}),console.log("_END_"),y;De(this.responseText)}},!1),e.apply(this,arguments)},0}window.addEventListener("scroll",async function(){var e,t,n=window.scrollY;if(document.documentElement.scrollHeight-1<=n+window.innerHeight){for([e,t]of await plx.getAll()){var i={Id:e,profileId:t.profileId,name:t.fullName,bio:t.bio,url:t.profileLink,image:t.imageSrc,group_id:t.groupId,group_joining_text:t.groupJoiningText,profile_type:t.profileType,created_at:(new Date).toISOString(),updated_at:(new Date).toISOString(),source:"facebook"};y.push(i)}await plx.clear()}},{passive:!0}),window.addEventListener("scrollend",()=>{y.forEach(e=>{console.log(JSON.stringify({Id:e.Id,profileId:e.profileId,name:e.name,bio:e.bio,url:e.url,image:e.image,group_id:e.group_id,group_joining_text:e.group_joining_text,profile_type:e.profile_type,created_at:(new Date).toISOString(),updated_at:(new Date).toISOString(),source:"facebook"}))}),console.log("_end_record_")}),Se(); """

TABLE_NAME_USERS = "facebook"
TABLE_NAME_GROUP = "facebook_groups"
TABLE_NAME_CHAT_GROUP = "facebook_chat_groups"
TABLE_NAME_SEND_MESSAGE = "facebook_message_sended"
TABLE_NAME_SEND_CHAT_MESSAGE = "facebook_group_message_sended"


class Facebook:

    def __init__(
        self,
        settings=None,
        database=None,
        output: QListView = None,
        reset: bool = False,
    ):
        if not reset:
            self.settings = settings
            self.database = database
            self.gListView = output
            self.helper = helper(self.gListView)

            self.database.create_table(TABLE_NAME_USERS)
            self.database.create_table(TABLE_NAME_GROUP)
            self.database.create_table(TABLE_NAME_CHAT_GROUP)

            if not os.path.isdir(f"{self.helper.CHROME_USER_DATA}/facebook"):
                with sync_playwright() as p:
                    browser = p.chromium.launch_persistent_context(
                        user_data_dir=f"{self.helper.CHROME_USER_DATA}/facebook",
                        headless=False,
                        args=[
                            "--no-sandbox",
                            "--disable-blink-features=AutomationControlled",
                            "--disable-features=IsolateOrigins,site-per-process",
                            "--disable-web-security",
                            "--disable-gpu",
                            "--disable-dev-shm-usage",
                        ],
                        slow_mo=500,
                    )
                    page = browser.pages[0] if browser.pages else browser.new_page()

                    user_agents = [
                        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
                        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
                        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
                    ]
                    page.set_extra_http_headers(
                        {"User-Agent": random.choice(user_agents)}
                    )
                    page.goto(self.helper.FACEBOOK_WEB, timeout=10000)
                    page.wait_for_load_state("networkidle")
                    self.helper.UpDateOutput("Start Facebook")

                    try:
                        # Wait for login button
                        page.wait_for_selector("//button[@name='login']", timeout=5000)
                        # Fill in email and password
                        page.fill(
                            "#email", "your_fb_username"
                        )  # Replace with self.settings["fb_username"]
                        page.fill(
                            "#pass", "your_fb_password"
                        )  # Replace with self.settings["fb_password"]
                        # Click the login button
                        page.click("//button[@name='login']")
                        # Show confirmation message
                        msg_box = QMessageBox()
                        msg_box.setWindowTitle("Confirmation")
                        msg_box.setText(
                            "This is First time only, after that you will log in normally"
                        )
                        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                        response = msg_box.exec()
                        if response == QMessageBox.No:
                            browser.close()
                    except Exception as e:
                        print("An error occurred:", e)
                    browser.close()

    def reset(self, userdata, setting):
        with sync_playwright() as p:
            browser = p.chromium.launch_persistent_context(
                user_data_dir=userdata,
                headless=False,
                args=[
                    "--no-sandbox",
                    "--disable-blink-features=AutomationControlled",
                    "--disable-features=IsolateOrigins,site-per-process",
                    "--disable-web-security",
                    "--disable-gpu",
                    "--disable-dev-shm-usage",
                ],
                slow_mo=500,
            )
            page = browser.pages[0] if browser.pages else browser.new_page()
            user_agents = [
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
            ]
            page.set_extra_http_headers({"User-Agent": random.choice(user_agents)})
            page.goto("https://facebook.com", timeout=10000)
            page.wait_for_load_state("networkidle")
            try:
                # Wait for login button
                page.wait_for_selector("//button[@name='login']", timeout=5000)
                # Fill in email and password
                page.fill(
                    "#email", setting.value("fb_username")
                )  # Replace with self.settings["fb_username"]
                page.fill(
                    "#pass", setting.value("fb_password")
                )  # Replace with self.settings["fb_password"]
                # Click the login button
                page.click("//button[@name='login']")
                # Show confirmation message
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Confirmation")
                msg_box.setText(
                    "This is First time only, after that you will log in normally"
                )
                msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                response = msg_box.exec()
                if response == QMessageBox.No:
                    return False
                else:
                    return True

            except Exception as e:
                print("An error occurred:", e)
                return False
            finally:
                browser.close()

    async def is_logout(self, page) -> bool:
        try:
            # Select the element by its id
            login_form = page.locator("#login_popup_cta_form")
            # Wait for the element to be visible
            await login_form.wait_for(state="visible", timeout=10000)

            # Interact with the element (e.g., click it)
            await login_form.click()

            # Example: Fill an input field inside the form
            email_input = login_form.locator('input[type="text"][name="email"]')
            await email_input.fill(self.settings["fb_username"])

            password_input = login_form.locator('input[type="password"][name="pass"]')
            await password_input.fill(self.settings["fb_password"])

            # Submit the form
            submit_button = login_form.locator(
                'div[role="button"][aria-label="Accessible login button"]'
            )
            await submit_button.click()
            return True

        except Exception:
            return False

    async def post_to_groups(
        self,
        list_of_groups,
        category,
        message,
        useAI=False,
        CompanName: str = None,
        Slogin: str = None,
    ):
        try:
            ListOfMessages = []
            self.helper.UpDateOutput("Waiting initialization Facebook Group...")
            if CompanName:
                loop_time = 0
                while len(ListOfMessages) == 0:
                    if loop_time >= 50:
                        ListOfMessages = []
                        break
                    else:
                        loop_time += 1

                    ListOfMessages = self.database.get_msg_history(CompanName)
                    await asyncio.sleep(randrange(4, 10))

            async with async_playwright() as p:

                browser = await p.chromium.launch_persistent_context(
                    user_data_dir=self.helper.CHROME_USER_DATA + "/facebook",
                    headless=True,
                    args=[
                        "--no-sandbox",
                        "--disable-blink-features=AutomationControlled",
                        "--disable-features=IsolateOrigins,site-per-process",
                        "--disable-web-security",
                    ],
                )
                page = browser.pages[0] if browser.pages else await browser.new_page()
                user_agents = [
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
                ]

                selected_user_agent = random.choice(user_agents)
                # selected_user_agent = random.choice(user_agents)
                await page.set_extra_http_headers({"User-Agent": selected_user_agent})
                await page.set_viewport_size({"width": 830, "height": 930})
                if list_of_groups is None:
                    list_of_groups = self.database.search_by_column(
                        TABLE_NAME_GROUP, "category", category
                    )

                basic_group_link = "https://facebook.com/groups/"
                countPost = 0
                DateNow = str(datetime.date.today().strftime("%d/%m/%Y"))

                for group in list_of_groups:
                    try:
                        TimeNow = int(time.time())
                        if len(group) == 0:
                            continue

                        group_number = re.search(
                            r"^https:\/\/www\.facebook\.com\/groups\/([a-zA-Z0-9.-]+)",
                            group,
                        )
                        group = group_number.group(1)
                        if group != "" or not group is None:
                            if self.database.search_by_columns(
                                TABLE_NAME_SEND_CHAT_MESSAGE,
                                "group_id",
                                group,
                                "date",
                                DateNow,
                            ):
                                self.helper.UpDateOutput(
                                    f"Skip {group} we post on it today..."
                                )
                                continue
                        else:
                            continue

                        if countPost >= 30:
                            self.helper.UpDateOutput(
                                "We will hold 30min for un-block account."
                            )
                            await asyncio.sleep(1800)
                            countPost = 0

                        group_id = (
                            group if isinstance(group, str) else group["group_id"]
                        )

                        GroupURL = f"{basic_group_link}{group_id}"

                        self.helper.UpDateOutput(f"Open Group {GroupURL}")

                        await page.goto(
                            GroupURL, timeout=120000, wait_until="domcontentloaded"
                        )

                        if await self.is_logout(page):
                            ok = QMessageBox.warning(
                                None,
                                "Warning",
                                "Please login to Facebook, and Confirm it , after that Click On OK button",
                                QMessageBox.Ok,
                            )
                            if ok:
                                browser.close()
                                return

                        self.helper.UpDateOutput("Writing Post...")

                        self.helper.UpDateOutput("Select Message for Post...")
                        if len(ListOfMessages) > 0:
                            send_message = ListOfMessages[
                                randrange(0, len(ListOfMessages))
                            ].get("message")
                        else:
                            send_message = message.strip()

                        if send_message == "":
                            send_message = message.strip()

                        if not Slogin is None:
                            _slogin = Slogin.split("|")
                            if _slogin[0] == 0:
                                send_message = f"{ _slogin[1:]}\n\n {send_message}"
                            else:
                                send_message = f"{ send_message}\n\n {_slogin[1]}"

                        try:
                            element_xpath = f"//a[contains(@href, '/groups/{group_id}/buy_sell_discussion/') and @role='tab']"
                            descriptionTab = page.locator(f"xpath={element_xpath}")
                            # descriptionTab = page.get_by_text('Discussion').and_(page.get_by_role('tab'))
                            await descriptionTab.wait_for(state="visible", timeout=6000)
                            await descriptionTab.scroll_into_view_if_needed()
                            if descriptionTab:
                                await descriptionTab.click(force=True)
                        except Exception:
                            pass

                        self.helper.UpDateOutput(f"Message Select is {send_message}...")
                        Selector = ""
                        try:
                            Selector = ":is(div[role='textbox'][aria-label*='Create a public post...'], span:has-text('Write something...'))"

                            textarea_selector = await page.wait_for_selector(
                                Selector, state="visible", timeout=10000
                            )
                        except:
                            Selector = "span:has-text('Write something...')"
                            textarea_selector = await page.wait_for_selector(
                                Selector, state="visible", timeout=20000
                            )

                        await textarea_selector.scroll_into_view_if_needed()
                        await asyncio.sleep(randrange(1, 3))
                        await textarea_selector.click(force=True)
                        await asyncio.sleep(randrange(2, 6))
                        # page.get_by_label('Post anonymously').check()
                        text = await textarea_selector.inner_text()
                        if "Write something" in text:
                            # await page.keyboard.press("Control+V")
                            await page.evaluate("(el) => el.focus()", textarea_selector)
                            if len(send_message) > 20:
                                pyperclip.copy(send_message)
                                await textarea_selector.focus()
                                await page.keyboard.insert_text(send_message)
                                await page.keyboard.press("Shift+Enter", delay=1000)
                            else:
                                await textarea_selector.press("Enter")
                                await page.keyboard.type(send_message, delay=60)
                            try:
                                self.helper.UpDateOutput("Posted...")
                                await page.evaluate(
                                    "document.querySelector('span.x1lliihq').style.display='none'"
                                )
                                post_button = await page.wait_for_selector(
                                    'div[aria-label="Post"][role="button"]',
                                    timeout=60000,
                                )
                                await post_button.scroll_into_view_if_needed()
                                await post_button.click(force=True)
                                self.helper.UpDateOutput("Uploading Post...")
                                # await page.screenshot(path=f"Output/Confirmation_{group_id}.png")
                                await asyncio.sleep(randrange(5, 10))
                            except:
                                logging.error("Error : \n" + traceback.format_exc())
                                continue
                        else:
                            self.helper.UpDateOutput(f"Error in Post Group {group_id}")
                            continue
                    except Exception:
                        self.helper.UpDateOutput(f"Error in Post Group {group_id}")
                        logging.error("Error : \n" + traceback.format_exc())
                        continue

                    self.database.write_to_database(
                        TABLE_NAME_SEND_CHAT_MESSAGE,
                        {
                            "group_id": group,
                            "name": (
                                group if isinstance(group, str) else group["group_name"]
                            ),
                            "message": send_message,
                            "category": category,
                            "date": DateNow,
                            "time": TimeNow,
                        },
                    )
                    self.database.save_msg_or_post(
                        user=group_id, message=send_message, source="FBG"
                    )
                    self.helper.UpDateOutput(f"Saved {group_id}")
                    countPost += 1
        except Exception:
            logging.error("Error : \n" + traceback.format_exc())
            return False
        finally:
            self.helper.UpDateOutput("==== Send Posts is Done... ====")
            if await browser.is_connected():
                await browser.close()
            return True

    async def get_group_members(self, category, group_name: str):
        async with async_playwright() as p:
            browser = await p.chromium.launch_persistent_context(
                user_data_dir=self.helper.CHROME_USER_DATA + "/facebook",
                headless=True,
                args=[
                    "--no-sandbox",
                    "--disable-blink-features=AutomationControlled",
                    "--disable-features=IsolateOrigins,site-per-process",
                    "--disable-web-security",
                ],
            )
            page = browser.pages[0] if browser.pages else await browser.new_page()
            user_agents = [
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
            ]

            selected_user_agent = random.choice(user_agents)
            await page.set_extra_http_headers({"User-Agent": selected_user_agent})

            if self.helper.is_file_path(group_name):
                list_of_groups = self.helper.readlist_file(group_name)
            elif group_name == "":
                list_of_groups = self.database.select_column(
                    "facebook_groups", "group_name"
                )
            elif isinstance(group_name, str):
                inlist = f"{group_name},".split(",")
                list_of_groups = list(filter(None, inlist))
            else:
                self.helper.UpDateOutput("Error in Facebook group list")
                return

            for group in list_of_groups:
                url_group = f"https://m.facebook.com/groups/{group}/members"
                await page.goto(url_group, timeout=120000)
                await asyncio.sleep(randrange(1, 5))
                messages = []

                GroupName = list(
                    filter(None, await page.get_by_role("link").all_text_contents())
                )[0]
                self.helper.UpDateOutput(f"Open Group Name:{GroupName}")

                def handle_console_message(msg):
                    messages.append(msg.text)
                    MemberCount = len(messages) * 10
                    self.helper.UpDateOutput(f"Scan Group Members...({MemberCount})")

                page.on("console", handle_console_message)
                await page.evaluate_handle(FB_SCRIPT)

                if isinstance(GroupName, str):
                    if not GroupName == "":
                        self.database.write_to_database(
                            TABLE_NAME_GROUP,
                            {
                                "group_id": group,
                                "group_name": GroupName,
                                "category": category,
                            },
                        )
                    else:
                        self.database.write_to_database(
                            TABLE_NAME_GROUP,
                            {
                                "group_id": group,
                                "group_name": "Unknown",
                                "category": category,
                            },
                        )
                NextNumber = 0
                CurrentNumber = 0
                Tryloop = 0
                while True:
                    await asyncio.sleep(8)
                    CurrentNumber = messages.count("_end_record_")
                    if NextNumber > CurrentNumber:
                        if Tryloop >= 3:
                            break
                        else:
                            Tryloop += 1
                    else:
                        NextNumber = CurrentNumber + 2
                        Tryloop = 0

                # countItem = 1
                for msg in messages:
                    if "_end_record_" in msg or "console.clear" in msg:
                        continue
                    else:
                        if msg.startswith('"{\\"id') or "group_joining_text" in msg:
                            json_object = json.load(StringIO(msg))
                            if isinstance(json_object, dict):
                                json_object["category"] = category
                                json_object["group_joining_text"] = (
                                    self.helper.convert_to_datetime(
                                        json_object["group_joining_text"]
                                    )
                                )
                                if not self.database.search_by_column(
                                    TABLE_NAME_USERS,
                                    "profileId",
                                    json_object["profileId"],
                                ):
                                    self.database.write_to_database(
                                        TABLE_NAME_USERS, json_object
                                    )
                                    self.helper.UpDateOutput(
                                        f"Add {json_object['name']}"
                                    )
                                else:
                                    self.database.update_in_database(
                                        TABLE_NAME_USERS,
                                        {"profileId": json_object["profileId"]},
                                        {
                                            "group_joining_text": json_object[
                                                "group_joining_text"
                                            ]
                                        },
                                    )
                                    self.helper.UpDateOutput(
                                        f"Update {json_object['name']}"
                                    )

                            else:
                                self.helper.UpDateOutput(
                                    "Error fb-223 : Not a dictionary"
                                )

            await browser.close()

    async def send_to_members(
        self,
        message: str,
        category: str,
        filePath: str = None,
        useing_AI=False,
        CompanName: str = None,
        Slogin: str = None,
    ):
        ListOfMessages = []
        if CompanName:
            while len(ListOfMessages) == 0:
                ListOfMessages = self.database.get_msg_history(CompanName)
                sleep(10)

        countSend = 0
        if useing_AI:
            if len(ListOfMessages) > 0:
                send_message = ListOfMessages[randrange(0, len(ListOfMessages))][
                    "message"
                ]
            else:
                send_message = message
        else:
            send_message = message

        if not Slogin is None:
            _slogin = Slogin.split("|")
            if _slogin[0] == 0:
                send_message = f"{ _slogin[1]}\n\n {send_message}"
            else:
                send_message = f"{ send_message}\n\n {_slogin[1]}"

        self.database.create_table(TABLE_NAME_SEND_MESSAGE)
        self.helper.UpDateOutput("Get Users...")
        users = self.database.search_by_column(TABLE_NAME_USERS, "category", category)
        for user in users:
            if countSend >= 20:
                self.helper.UpDateOutput(
                    "We are send 20 Message we will hold 1h for un-Block account"
                )
                sleep(3600)
                countSend = 0
            self.helper.UpDateOutput(f"{countSend} Name: {user['name']}")
            self.helper.UpDateOutput(f"Open Message with {user['name']}")

            async with async_playwright() as p:
                browser = await p.chromium.launch_persistent_context(
                    user_data_dir=self.helper.CHROME_USER_DATA + "/facebook",
                    headless=True,
                    args=[
                        "--no-sandbox",
                        "--disable-blink-features=AutomationControlled",
                        "--disable-features=IsolateOrigins,site-per-process",
                        "--disable-web-security",
                    ],
                )
                page = browser.pages[0] if browser.pages else await browser.new_page()
                user_agents = [
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
                ]

                selected_user_agent = random.choice(user_agents)
                # selected_user_agent = random.choice(user_agents)
                await page.set_extra_http_headers({"User-Agent": selected_user_agent})

                try:
                    # Navigate to the user's profile
                    await page.goto(user["url"], wait_until="domcontentloaded")
                    send_message = ListOfMessages[randrange(0, len(ListOfMessages))][
                        "message"
                    ]
                    if len(ListOfMessages) > 0:
                        while True:
                            old_message = self.database.search_by_columns(
                                "total_msg_post",
                                "user",
                                user["name"],
                                "message",
                                send_message,
                            )
                            if not old_message:
                                break
                            else:
                                send_message = ListOfMessages[
                                    randrange(0, len(ListOfMessages))
                                ]["message"]
                    else:
                        send_message = message

                    # await page.screenshot(path=os.path.join(os.path.dirname(__file__), "..") + "/user_profile.png")
                    send_message = f"Hey {user['name']}...\n{send_message}"
                    self.helper.UpDateOutput(
                        f"Message for {user['name']} is {send_message}"
                    )
                    # Wait for the "Message" button and click it
                    message_button = await page.wait_for_selector(
                        '//div[@aria-label="Message"]', timeout=10000
                    )
                    await message_button.click()
                    # await page.screenshot(path=f"{user['name']}_0.png")
                    # Wait for message input box
                    message_box = await page.wait_for_selector(
                        '//div[@aria-label="Message" and @role="textbox"]',
                        timeout=10000,
                    )
                    # await page.screenshot(path=f"{user['name']}_1.png")

                    # Copy message to clipboard and paste
                    pyperclip.copy(send_message)
                    await message_box.focus()
                    # await page.keyboard.press("Control+V")
                    # await page.keyboard.type(send_message, delay=50)
                    await page.keyboard.insert_text(send_message)
                    await page.keyboard.press("Shift+Enter", delay=1000)
                    # await page.screenshot(path=f"{user['name']}_2.png")
                    await asyncio.sleep(5)
                    # Save message to the database
                    self.database.write_to_database(
                        "send_message_table",
                        {
                            "profileID": user["profileId"],
                            "name": user["name"],
                            "message": send_message,
                        },
                    )
                    self.database.save_msg_or_post(
                        user=user["name"], message=send_message, source="FBM"
                    )
                    # Send the message (Press Enter)
                    await page.keyboard.press("Enter")
                    await page.keyboard.press("Enter", delay=500)
                    # print(f"Message sent successfully to {user['name']}.")
                    await asyncio.sleep(5)
                    # await page.screenshot(path=f"{user['name']}_3.png")

                except Exception as e:
                    logging.error("Error : \n" + traceback.format_exc())
                    continue
                finally:
                    await browser.close()

    # def send_to_group_chat(self, category: str, list_of_chat_groups: str=None):
    #     if self.driver is None:
    #         self.helper.UpDateOutput("Driver is None")
    #         return
    #     self.driver.set_window_size(1200, 650)
    #     self.database.create_table(TABLE_NAME_SEND_CHAT_MESSAGE)
    #     try:
    #         if list_of_chat_groups is None:
    #             chats = self.database.search_by_column(
    #                 TABLE_NAME_CHAT_GROUP, "category", category
    #             )
    #         else:
    #             if self.helper.is_file_path(list_of_chat_groups):
    #                 chats = self.helper.readlist_file(list_of_chat_groups)
    #             else:
    #                 chats = list_of_chat_groups.split(",")

    #         for chat_number in chats:
    #             try:
    #                 url_group_chat = (
    #                     f"https://www.facebook.com/messages/t/{chat_number}"
    #                 )
    #                 sleep(randrange(5))
    #                 user_message = self.settings["message"]
    #                 if not self.database.search_by_columns(
    #                     TABLE_NAME_SEND_CHAT_MESSAGE,
    #                     column1="groupId",
    #                     column2="message",
    #                     value1=chat_number,
    #                     value2=user_message,
    #                 ):
    #                     self.driver.get(url_group_chat)
    #                     self.database.write_to_database(
    #                         TABLE_NAME_CHAT_GROUP,
    #                         {"groupId": chat_number, "category": category},
    #                     )
    #                     message = WebDriverWait(self.driver, randrange(10)).until(
    #                         EC.presence_of_element_located(
    #                             (
    #                                 By.XPATH,
    #                                 '//div[@aria-label="Message" and @role="textbox"]',
    #                             )
    #                         )
    #                     )
    #                     for line in user_message.split("\n"):
    #                         pyperclip.copy(line)
    #                         message.send_keys(Keys.CONTROL, "v")
    #                         message.send_keys(Keys.SHIFT, Keys.ENTER)
    #                     self.database.write_to_database(
    #                         TABLE_NAME_SEND_CHAT_MESSAGE,
    #                         {"groupId": chat_number, "message": user_message},
    #                     )
    #                     sleep(randrange(1, 3))
    #                     message.send_keys(Keys.RETURN)
    #                     sleep(randrange(5, 10))
    #             except Exception as e:
    #                 self.helper.UpDateOutput(f"Pass Group ID {chat_number}")
    #                 continue
    #         # end for
    #     except Exception as e:
    #         logging.error("Error : \n" + traceback.format_exc())
    #     finally:
    #         self.driver.close()

    #     pass
