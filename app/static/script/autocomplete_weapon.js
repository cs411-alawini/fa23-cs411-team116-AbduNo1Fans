let availableWeapons = [
    'STRONG-ARM (HANDS, FIST, FEET OR BODILY FORCE)',
    'UNKNOWN WEAPON/OTHER WEAPON',
    'VERBAL THREAT',
    'ROCK/THROWN OBJECT',
    'AIR PISTOL/REVOLVER/RIFLE/BB GUN',
    'FOLDING KNIFE',
    'RAZOR',
    'BLUNT INSTRUMENT',
    'BOTTLE',
    'OTHER CUTTING INSTRUMENT',
    'HAND GUN',
    'PHYSICAL PRESENCE',
    'VEHICLE',
    'SCISSORS',
    'STICK',
    'MACHETE',
    'OTHER KNIFE',
    'MACE/PEPPER SPRAY',
    'KNIFE WITH BLADE 6INCHES OR LESS',
    'FIRE',
    'SEMI-AUTOMATIC PISTOL',
    'GLASS',
    'SIMULATED GUN',
    'KNIFE WITH BLADE OVER 6 INCHES IN LENGTH',
    'DEMAND NOTE',
    'BOMB THREAT',
    'PIPE/METAL PIPE',
    'ICE PICK',
    'UNKNOWN FIREARM',
    'STUN GUN',
    'KITCHEN KNIFE',
    'SCREWDRIVER',
    'SHOTGUN',
    'BELT FLAILING INSTRUMENT/CHAIN',
    'HAMMER',
    'SEMI-AUTOMATIC RIFLE',
    'UNKNOWN TYPE CUTTING INSTRUMENT',
    'BRASS KNUCKLES',
    'FIXED OBJECT',
    'REVOLVER',
    'SWITCH BLADE',
    'CLUB/BAT',
    'AXE',
    'RIFLE',
    'ASSAULT WEAPON/UZI/AK47/ETC',
    'OTHER FIREARM',
    'ANTIQUE FIREARM',
    'HECKLER & KOCH 93 SEMIAUTOMATIC ASSAULT RIFLE',
    'CONCRETE BLOCK/BRICK',
    'BOARD',
    'SAWED OFF RIFLE/SHOTGUN',
    'BOW AND ARROW',
    'SWORD',
    'STARTER PISTOL/REVOLVER',
    'RAZOR BLADE',
    'SCALDING LIQUID',
    'DIRK/DAGGER',
    'TIRE IRON',
    'CAUSTIC CHEMICAL/POISON',
    'TOY GUN',
    'CLEAVER',
    'LIQUOR/DRUGS',
    'EXPLOXIVE DEVICE',
    'ROPE/LIGATURE',
    'MARTIAL ARTS WEAPONS',
    'AUTOMATIC WEAPON/SUB-MACHINE GUN',
    'DOG/ANIMAL (SIC ANIMAL ON)',
    'SYRINGE',
    'UZI SEMIAUTOMATIC ASSAULT RIFLE',
    'MAC-10 SEMIAUTOMATIC ASSAULT WEAPON',
    'BLACKJACK',
    'MAC-11 SEMIAUTOMATIC ASSAULT WEAPON',
    'BOWIE KNIFE',
    'STRAIGHT RAZOR',
    'M1-1 SEMIAUTOMATIC ASSAULT RIFLE',
    'HECKLER & KOCH 91 SEMIAUTOMATIC ASSAULT RIFLE',
    'RELIC FIREARM',
    'UNK TYPE SEMIAUTOMATIC ASSAULT RIFLE',
];

const weaponvalid_results = document.querySelector(".weaponvalid_results");
const weaponcode_input = document.getElementById("weaponcode_input");

weaponcode_input.onkeyup = function(){
    let result = []; 
    let input = weaponcode_input.value; //filter
    if(input.length){
        result = availableWeapons.filter((keyword)=>{
            return keyword.toLowerCase().includes(input.toLowerCase());
        });
        console.log(result);
    }
    displayWeapon(result);
    if(!result.length){
        weaponvalid_results.innerHTML = '';
    }
}

function displayWeapon(result){
    const content = result.map((list)=>{
        return "<li onclick=selectInputWeapon(this)>" + list + "</li>";
    });
    weaponvalid_results.innerHTML = "<ul>" + content.join('') + "</ul>";
}

function selectInputWeapon(list){
    weaponcode_input.value = list.innerHTML;
    weaponvalid_results.innerHTML = '';
}